import sys

import ply.yacc as yacc
from expression_lex import tokens

def p_exp1(p):
    "exp : term"
    p[0] = p[1]

def p_exp2(p):
    "exp : exp term"
    if p[2] == "":
        p[0] = p[1]
    else:
        p[0] = p[1] + p[2]

#
#def p_exp3(p):
#    """exp : exp OPAD term"""
#    if p[2] == "":
#        p[0] = p[1]
#    else:
#        p[0] = p[1] + ",\n" + p[2]
#


def p_term1(p):
    "term : fact"
    p[0] = p[1]

def p_term3(p):
    "term : term fact"
    if p[2] == "":
        p[0] = p[1]
    else:
        p[0] = p[1] + p[2]




    
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
parser.id_table = { }
parser.id_count = 0

source = ""
for linha in sys.stdin:
    source += linha
codigo = parser.parse(source)
if parser.success:
    print('Parsing completed!')
    print(codigo)
else:
    print('Parsing failed!')