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
    'SWAP',
    'KEY',
    'IF',
    'ELSE',
    'THEN',
    'DEPTH',
    'DROP',
    'DO',
    'LOOP',
    'PLUSLOOP',
    'ITERATION',
    'VARIABLE',
    'COMMENT',
    'WORD'
)

literals = ['.',':',';','!','@']


def t_COMMENT(t):
    r'\(\s.*\)'
    t.value = re.match(r'\(\s(.*)\)', t.value).group(1)
    return t

def t_CHAR(t):
    r'(?i)\bCHAR\b\s+\S+'
    t.value = re.match(r'(?i)\bCHAR\b\s+(\S+)', t.value).group(1)
    return t

def t_INT(t):
    r'(?P<sign>\+|-)?(\d+)(?=(?(sign)\s|[\+\-\*\/]?\s))'
    return t

def t_NAME(t):
    r'(?<=:\s)(\S+)(?=[\S\s]*;[^\S])'
    return t

def t_DOTQUOTE(t):
    r'\."\s[\S\s]*?"'
    t.value = re.match(r'(\."\s)([\S\s]*?)(")', t.value).group(2)
    return t

def t_EMIT(t):
    r'(?i)\bEMIT\b'
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

def t_SWAP(t):
    r'(?i)\bSWAP\b'
    return t

def t_KEY(t):
    r'(?i)\bKEY\b'
    return t

def t_IF(t):
    r'(?i)\bIF\b'
    return t

def t_ELSE(t):
    r'(?i)\bELSE\b'
    return t

def t_THEN(t):
    r'(?i)\bTHEN\b'
    return t

def t_DEPTH(t):
    r'(?i)\bDEPTH\b'
    return t

def t_DROP(t):
    r'(?i)\bDROP\b'
    return t

def t_DO(t):
    r'(?i)\bDO\b'
    return t

def t_LOOP(t):
    r'(?i)\bLOOP\b'
    return t

def t_PLUSLOOP(t):
    r'(?i)\b\+LOOP\b'
    return t

def t_ITERATION(t):
    r'(?i)\bi\b'
    return t


def t_VARIABLE(t):
    r'(?i)\bVARIABLE\b'
    return t

def t_OPR(t):
    r'(\+|\-|\*|\/|\%|==|!=|<=|>=|<|>)'
    return t

def t_WORD(t):
    r'([\S]{2,}|[a-zA-Z])\S*'
    t.value = str(t.value)
    return t


t_ignore = ' \n\t'

def t_error(t):
    print(f"Carácter ilegal {t.value[0]}")
    t.lexer.skip(1)



lexer = lex.lex()