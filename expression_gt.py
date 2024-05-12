import sys

import ply.yacc as yacc
from expression_lex import tokens

def p_exp_empty(p):
    'exp : '
    p[0] = ''

def p_exp(p):
    """exp : term exp
           | function exp
           | conditional exp
           | loop exp
           | variable exp
    """
    p[0] = p[1] + p[2]
    

def p_term(p):
    "term : fact"
    p[0] = p[1]
    parser.word_count += 1

def p_function(p):
    "function : ':' NAME exp ';'"
    if p[2] in parser.func or p[2] in parser.var:
        print(f"Word {parser.word_count}: Duplicate name")
        parser.success = False
    else:
        parser.func.update({p[2]: f"{p[3]}"})
        parser.word_count += 2
        p[0] = ""

def p_conditional(p):
    "conditional : IF exp ELSE exp THEN"
    p[0] = f'jz ELSE{parser.else_count}\n{p[2]}ELSE{parser.else_count}:\n{p[4]}ENDIF{parser.else_count}:'
    parser.else_count += 1
    parser.word_count += 2

def p_loop(p):
    "loop : DO exp LOOP"
    p[0] = f"""
STOREG {parser.var_count}
STOREG {parser.var_count+1}
WHILE{parser.var_count}:
{p[2]}PUSHG {parser.var_count}
PUSHG {parser.var_count+1}
SUP
JZ ENDWHILE{parser.var_count}
PUSHI 1
SUB
STOREG {parser.var_count}
JUMP WHILE{parser.var_count}
ENDWHILE{parser.var_count}:
"""
    parser.var_count += 2
    parser.word_count += 2


def p_plusloop(p):
    "loop : DO exp PLUSLOOP"
    p[0] = f"""
STOREG {parser.var_count}
STOREG {parser.var_count+1}
WHILE{parser.var_count}:
PUSHG {parser.var_count}
PUSHG {parser.var_count+1}
SUP
JZ ENDWHILE{parser.var_count}{p[2]}
PUSHI 1
SUB
STOREG {parser.var_count}
JUMP WHILE{parser.var_count}
ENDWHILE{parser.var_count}:
"""
    parser.var_count += 2
    parser.word_count += 2


def p_variable1(p):
    "variable : VARIABLE WORD"
    if p[2] in parser.func or p[2] in parser.var:
        print(f"Word {parser.word_count}: Duplicate name")
        parser.success = False
    else:
        parser.var.update({p[2]: f'{parser.var_count}'})
        parser.var_count += 1
        p[0] = ""
        for key in parser.func:
            print(key)

def p_variable2(p):
    "variable : WORD '!'"
    if p[1] not in parser.var:
        print(f"Word {parser.word_count}: Undefined name")
        parser.success = False
    else:
        p[0] = f"STOREG {parser.var[p[1]]}\n"
        parser.word_count += 1

def p_variable3(p):
    "variable : WORD '@'"
    if p[1] not in parser.var:
        print(f"Word {parser.word_count}: Undefined name")
        parser.success = False
    else:
        p[0] = f"PUSHG {parser.var[p[1]]}\n"
        parser.word_count += 1



def p_factOPR(p):
    "fact : OPR"
    if p[1] == '+':
        p[0] = 'ADD\n'
    elif p[1] == '-':
        p[0] = 'SUB\n'
    if p[1] == '*':
        p[0] = 'MUL\n'
    elif p[1] == '/':
        p[0] = 'DIV\n'
    elif p[1] == '%':
        p[0] = 'MOD\n'
    elif p[1] == '==':
        p[0] = 'EQUAL\n'
    elif p[1] == '!=':
        p[0] = 'EQUAL NOT\n'
    elif p[1] == '<':
        p[0] = 'INF\n'
    elif p[1] == '<=':
        p[0] = 'INFEQ\n'
    elif p[1] == '>':
        p[0] = 'SUP\n'
    elif p[1] == '>=':
        p[0] = 'SUPEQ\n'
    parser.stack_size -= 2



def p_factInt(p):
    "fact : INT"
    p[0] = "PUSHI " + p[1] + "\n"
    parser.stack_size += 1


def p_factWord(p):
    "fact : WORD"
    if p[1] in parser.func:
        p[0] = f"{p[1]}:\n\t{parser.func[p[1]]}\n"
    else:
        p[0] = ""
        parser.success = False
        if (p[1] == "CHAR"):
            print(f"Word {parser.word_count}: Unterminated string")
        else:
            print(f"Word {parser.word_count}: Undefined name")


def p_factComment(p):
    "fact : COMMENT"
    p[0] = "    // " + p[1]

def p_factDOT(p):
    "fact : '.'"
    p[0] = "WRITEI\n"
    parser.stack_size -= 1

def p_factDOTQUOTE(p):
    "fact : DOTQUOTE"
    p[0] = 'PUSHS "' + p[1] + '"\nWRITES\n'

def p_factEMIT(p):
    "fact : EMIT"
    p[0] = "WRITECHR\n"
    parser.stack_size -= 1

def p_factCHAR(p):
    "fact : CHAR"
    p[0] = f"PUSHS {p[1]}\nCHRCODE\n"


def p_factDUP(p):
    "fact : DUP"
    p[0] = "DUP 1\n"
    parser.stack_size += 1

def p_factCR(p):
    "fact : CR"
    p[0] = "WRITELN\n"

def p_factSPACE(p):
    "fact : SPACE"
    p[0] = 'PUSHS " "\nWRITES\n'
    

def p_factSPACES(p):
    "fact : SPACES"
    p[0] = f"""SPACES{parser.spaces_count}:
PUSHI 1
SUB
PUSHS " "
WRITES
DUP 1
NOT jz SPACES{parser.spaces_count}
POP 1
"""


def p_factSWAP(p):
    "fact : SWAP"
    p[0] = "SWAP\n"


def p_factKey(p):
    "fact : KEY"
    p[0] = "READ\n"
    parser.stack_size += 1


def p_factDEPTH(p):
    "fact : DEPTH"
    p[0] = f"PUSHI {parser.stack_size}\n"
    parser.stack_size += 1


def p_factDROP(p):
    "fact : DROP"
    p[0] = "POP 1\n"
    parser.stack_size -= 1


def p_factITER(p):
    "fact : ITERATION"
    p[0] = f"PUSHG {parser.var_count}"
    parser.stack_size += 1



def p_error(p):
    print("Syntax error in input!",p)
    parser.success=False




parser = yacc.yacc()
parser.success = True

parser.func = {}
parser.var = {}
parser.word_count = 0
parser.else_count = 0
parser.stack_size = 0
parser.var_count = 0
parser.spaces_count = 0




with open('input.txt', 'r') as file:
    source = file.read()

codigo = parser.parse(source)

with open('output.txt','w') as f:
    if parser.success:
        print('Parsing completed!')
        for i in range(parser.var_count):
                f.write("PUSHI 0\n")
        f.write("\nSTART\n\n")
        f.write(codigo)
        f.write("\nSTOP\n")
    else:
        print('Parsing failed!')