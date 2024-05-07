import sys

import ply.yacc as yacc
from expression_lex import tokens



def p_exp1(p):
    """exp : term
           | function
           | conditional
    """
    p[0] = p[1] + "STOP\n"

def p_exp2(p):
    "exp : exp term"
    if p[2] == "":
        p[0] = p[1]
    else:
        p[0] = p[1] + p[2]

def p_exp3(p):
    "exp : exp function"
    if p[2] == "":
        p[0] = p[1]
    else:
        p[0] = p[1] + p[2]

def p_exp4(p):
    "exp : exp conditional"
    if p[2] == "":
        p[0] = p[1]
    else:
        p[0] = p[1] + p[2]


def p_term1(p):
    "term : fact"
    p[0] = p[1]
    parser.word_count += 1


def p_functions1(p):
    "function : ':' NAME ';'"
    if p[2] in parser.func:
        print(f"Word {parser.word_count}: Duplicate name")
        parser.success = False
    else:
        parser.func.update({p[2]: "\nreturn\n"})
        parser.word_count += 2
        p[0] = ""

def p_functions2(p):
    "function : ':' NAME exp ';'"
    if p[2] in parser.func:
        print(f"Word {parser.word_count}: Duplicate name")
        parser.success = False
    else:
        parser.func.update({p[2]: f"{p[3]}return\n"})
        parser.word_count += 2
        p[0] = ""


def p_conditional1(p):
    "conditional : IF ELSE THEN"
    p[0] = f'jz ELSE{parser.else_count}\nELSE{parser.else_count}:\n'
    parser.else_count += 1


def p_conditional2(p):
    "conditional : IF exp ELSE THEN"
    p[0] = f'jz ELSE{parser.else_count}\n{p[2]}ELSE{parser.else_count}:\n'
    parser.else_count += 1


def p_conditional3(p):
    "conditional : IF ELSE exp THEN"
    p[0] = f'jz ELSE{parser.else_count}\nELSE{parser.else_count}:\n{p[3]}'
    parser.else_count += 1


def p_conditional4(p):
    "conditional : IF exp ELSE exp THEN"
    p[0] = f'jz ELSE{parser.else_count}\n{p[2]}ELSE{parser.else_count}:\n{p[4]}'
    parser.else_count += 1



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
    p[0] = p[1]
    if p[1] not in parser.func:
        print(f"Word {parser.word_count}: Undefined name")
        parser.success = False



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
    p[0] = 'PUSHS " "'
    

def p_factSPACES(p):
    "fact : SPACES"
    p[0] = "SPACES"



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




def p_error(p):
    print("Syntax error in input!",p)
    parser.success=False




parser = yacc.yacc()
parser.success = True

parser.func = {}
parser.word_count = 0
parser.else_count = 0
parser.stack_size = 0

source = ""
for linha in sys.stdin:
    source += linha
codigo = parser.parse(source)
if parser.success:
    print('Parsing completed!')
    print(codigo)
    for key, value in parser.func.items():
        print(f"{key}:")
        # Replace "\n" with "\n\t"
        modified_value = value.replace("\n", "\n\t")
        print("\t"+modified_value)
else:
    print('Parsing failed!')