import ply.lex as lex
import re

tokens = (
    'INT',
    'OPR',
    'NAME',
    'DOTQUOTE',
    'EMIT',
    'CHAR',
    'DUP',
    'CR',
    'SPACE',
    'SPACES',
    #'NUMBER_FLOAT',
    #'PLUS',
    #'MINUS',
    #'TIMES',
    #'DIVIDE',
    #'MOD',
    #'LPAREN',
    #'RPAREN',
    #'BSLASH',
    #'DOT',
    'COMMENT',
    'WORD'
)

literals = ['.',':',';']


def t_COMMENT(t):
    r'\(\s.*\)'
    t.value = re.match(r'\(\s(.*)\)', t.value).group(1)
    return t

#numbers
def t_INT(t):
    r'(?P<sign>\+|-)?(\d+)(?=(?(sign)\s|[\+\-\*\/]?\s))'
    return t


def t_NAME(t):
    r'(?<=:\s)(\S+)(?=.*;\s)'
    return t


def t_DOTQUOTE(t):
    r'\."\s[\S\s]*?"'
    t.value = re.match(r'(\."\s)([\S\s]*?)(")', t.value).group(2)
    return t

def t_EMIT(t):
    r'(?i)\bEMIT\b'
    return t

def t_CHAR(t):
    r'(?i)\bCHAR\b'
    return t

def t_DUP(t):
    r'(?i)\bDUP\b'
    return t

def t_CR(t):
    r'(?i)\bCR\b'
    return t

def t_SPACE(t):
    r'(?i)\bSPACE\b'
    return t

def t_SPACES(t):
    r'(?i)\bSPACES\b'
    return t

#need to change (ignore for now)
#def t_NUMBER_FLOAT(t):
#    r'\d+\.\d+'
#    t.value = float(t.value)
#    return t

##arithmetics
#def t_PLUS(t):
#    r'(\+)(?=\d*\s)'
#    t.value = "ADD"
#    return t
#
#def t_MINUS(t):
#    r'(\-)(?=\d*\s)'
#    t.value = "SUB"
#    return t
#
#def t_TIMES(t):
#    r'(\*)(?=\s)'
#    t.value = "MUL"
#    return t
#
#def t_DIVIDE(t):
#    r'(\/)(?=\s)'
#    t.value = "DIV"
#    return t
#
#def t_MOD(t):
#    r'(\%)(?=\s)'
#    t.value = "MOD"
#    return t
#
#
#def t_LPAREN(t):
#    r'\((?=\s)'
#    return t
#
#def t_RPAREN(t):
#    r'\)'
#    return t
#
#
#def t_BSLASH(t):
#    r'\\(?=\s)'
#    return t
#
#def t_DOT(t):
#    r'\.(?=\s)'
#    return t
#


def t_OPR(t):
    r'[\+\-\*\/\%]'
    return t

#words
def t_WORD(t):
    r'([\S]{2,}|[a-zA-Z])\S*'
    t.value = str(t.value)
    return t


t_ignore = ' \n\t'

def t_error(t):
    print(f"Carácter ilegal {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()


v = """
( fds )
"""

lexer.input(v)
for tok in lexer:
    print(tok)