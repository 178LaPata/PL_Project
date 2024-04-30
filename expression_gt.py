import sys

import ply.yacc as yacc
from expression_lex import tokens

def p_mano(p):
    "fds : fact"
    print("fds1")
    p[0] = p[1]

def p_fds1(p):
    "fds : fds fact"
    if p[2] == "":
        p[0] = p[1]
    else:
        p[0] = p[1] + ",\n" + p[2]

    
def p_factInt(p):
    "fact : INT"
    print("fact1")
    p[0] = "pushi " + p[1] + "\n"





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