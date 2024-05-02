import sys

import ply.yacc as yacc
from expression_lex import tokens



def p_exp1(p):
    """exp : term
           | function
    """
    p[0] = p[1]

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


def p_term1(p):
    "term : fact"
    p[0] = p[1]


def p_functions(p):
    "function : ':' NAME exp ';'"
    parser.func.update({p[2]: p[3]})
    p[0] = ""

 

def p_factInt(p):
    "fact : INT"
    p[0] = "pushi " + p[1] + "\n"


def p_factWord(p):
    "fact : WORD"
    p[0] = p[1]


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




def p_error(p):
    print("Syntax error in input!",p)
    parser.success=False




parser = yacc.yacc()
parser.success = True



parser.func = {}
parser.func_count = 0
parser.id_table = { }
parser.id_table.update()
parser.id_count = 0

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