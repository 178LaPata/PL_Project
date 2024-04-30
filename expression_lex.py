import ply.lex as lex

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
    'DOT',
    'WORD'
)



#numbers
def t_NUMBER_INT(t):
    r'([\+\-])?(\d+)(?=(?(1)[^\+\-\*\/\S]|[\+\-\*\/]?\s))'
    t.value = "PUSHI " + t.value
    return t

#need to change (ignore for now)
def t_NUMBER_FLOAT(t):
    r'\d+\.\d+'
    t.value = "PUSHF " + t.value
    return t


#arithmetics
def t_PLUS(t):
    r'(\+)(?=\d*\s)'
    t.value = "ADD"
    return t

def t_MINUS(t):
    r'(\-)(?=\d*\s)'
    t.value = "SUB"
    return t

def t_TIMES(t):
    r'(\*)(?=\s)'
    t.value = "MUL"
    return t

def t_DIVIDE(t):
    r'(\/)(?=\s)'
    t.value = "DIV"
    return t

def t_MOD(t):
    r'(\%)(?=\s)'
    t.value = "MOD"
    return t


#
def t_LPAREN(t):
    r'\((?=\s)'
    return t

def t_RPAREN(t):
    r'\)'
    return t


def t_BSLASH(t):
    r'\\(?=\s)'
    return t

def t_DOT(t):
    r'\.(?=\s)'
    return t


#words
def t_WORD(t):
    r'\S+'
    t.value = str(t.value)
    return t



t_ignore = ' \n\t'

def t_error(t):
    print(f"Carácter ilegal {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()


v = """
1+ 1- 2+ 2- 2* 2/
"""

lexer.input(v)
for tok in lexer:
    print(tok)