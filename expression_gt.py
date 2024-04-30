import sys

import ply.yacc as yacc
from expression_lex import tokens


    
def p_fact1(p):
    "fact : INT"
    p[0] = "pushi " + p[1] + "\n"
    return p




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
