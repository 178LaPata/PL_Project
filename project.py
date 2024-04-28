import ply.lex as lex
from ply import yacc

tokens = (
    'NUMBER_INT',
    'NUMBER_FLOAT',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'MOD',
    'LPAREN',
    'RPAREN',
    'BSLASH',
    'CARACTER',
    'DOT'
)

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_BSLASH = r'\\'
t_DOT = r'\.'

def t_NUMBER_INT(t):
    r'\d+'
    t.value = "PUSHI " + t.value
    return t

def t_NUMBER_FLOAT(t):
    r'\d+\.\d+'
    t.value = "PUSHF " + t.value
    return t

def t_PLUS(t):
    r'\+'
    t.value = "ADD"
    return t

def t_MINUS(t):
    r'\-'
    t.value = "SUB"
    return t

def t_TIMES(t):
    r'\*'
    t.value = "MUL"
    return t

def t_DIVIDE(t):
    r'\/'
    t.value = "DIV"
    return t

def t_MOD(t):
    r'\%'
    t.value = "MOD"
    return t

def t_CARACTER(t):
    r'\w+'
    t.value = str(t.value)
    return t

t_ignore = ' \n\t'

def t_error(t):
    print(f"Carácter ilegal {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()

v = """
123 456 + 789 - 123 * 456 / 789 % 123
"""

lexer.input(v)
for tok in lexer:
    print(tok)
