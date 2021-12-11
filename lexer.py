import ply.lex as lex
import sys
import re
# Tokens

reserved = {
    "if": "IF",
    "then": "THEN",
    "else": "ELSE",
    "while": "WHILE",
    "int": "INT",
    "char": "CHAR",
    "void": "VOID",
    "short": "SHORT",
    "long": "LONG",
    "float": "FLOAT",
    "double": "DOUBLE",
    "return": "RETURN",
    "break": "break",
    "struct": "struct",
}

literals = ['+', '-', '*', '/',
            '(', ')', '{', '}', '>', '<', ';', '=', '[', ']', '#', '.']

tokens = ["INCLUDE", "ID", "NUMBER", "GEQ", "LEQ", "STR",
          "CHR"] + list(reserved.values())

t_GEQ = r'>='
t_LEQ = r'<='
t_CHR = r"'.'"
t_STR = r'".*"'


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t


def t_INCLUDE(t):
    r'\#include[ \t]*(:?<|")\w*.h(:?>|")'
    t.value = re.search('(:?<|")\w*.h(:?>|")', t.value).group()[1:-1]
    return t


def t_COMMENT(t):
    r'//.*'
    pass


def t_LONGCOMMENT(t):
    r'/\*(.|\n)*\*/'
    pass


def t_NUMBER(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Invalid Token:", t.value[0])
    t.lexer.skip(1)


t_ignore = ' \t'

lexer = lex.lex()

if __name__ == "__main__":
    with open(sys.argv[-1]) as f:
        data = f.read()
    lexer.input(data)
    for tok in lexer:
        print(tok)