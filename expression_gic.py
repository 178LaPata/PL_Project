import sys

import ply.yacc as yacc
from expression_lex import tokens

#exp = expressions
#opad = operations adition
#OPMUL = operations multiplication


def p_grammar(p):
    """
    exp : term
        | exp term
        | exp OPAD term
    OPAD : '+' 
         | '-'
	term : fact
         | term OPMUL fact
    OPMUL : '*' 
          | '/'
    fact : INT 
         | WORD
         | '-' exp
    
    """


def p_error(p):
    print("Syntax error in input!",p)
    parser.success=False


parser = yacc.yacc()

for linha in sys.stdin:
    parser.success=True
    parser.parse(linha)
    if parser.success:
       print('Parsing completed!')
    else:
       print('Parsing failed!')
