# lexer.py

import re
from error import UslError

class Token:
    def __init__(self, type_, value, line):
        self.type = type_
        self.value = value
        self.line = line

    def __repr__(self):
        return f'Token({self.type}, {self.value}, line {self.line})'

TOKEN_SPEC = [
    ('COMMENT',  r'\#.*'),                   # Comments
    ('NEWLINE',  r'\n'),                     # Line endings
    ('SKIP',     r'[ \t]+'),                 # Skip spaces and tabs
    ('STRING',   r'"([^"\\]|\\.)*"'),        # String literal with escape sequences
    ('NUMBER',   r'\d+(\.\d*)?'),            # Integer or decimal number
    ('DEF',      r'\bdef\b'),                # Function definition
    ('CLASS',    r'\bclass\b'),              # Class definition
    ('EXTENDS',  r'\bextends\b'),            # Inheritance keyword
    ('RETURN',   r'\breturn\b'),             # Return keyword
    ('IF',       r'\bif\b'),                 # If keyword
    ('ELSE',     r'\belse\b'),               # Else keyword
    ('FOR',      r'\bfor\b'),                # For keyword
    ('WHILE',    r'\bwhile\b'),              # While keyword
    ('BREAK',    r'\bbreak\b'),              # Break keyword
    ('CONTINUE', r'\bcontinue\b'),           # Continue keyword
    ('IN',       r'\bin\b'),                 # In keyword
    ('NOT',      r'\bnot\b'),                # Not keyword
    ('AND',      r'\band\b'),                # And keyword
    ('OR',       r'\bor\b'),                 # Or keyword
    ('TRUE',     r'\bTrue\b'),               # True keyword
    ('FALSE',    r'\bFalse\b'),              # False keyword
    ('EQ',       r'=='),                     # Equal operator
    ('NEQ',      r'!='),                     # Not equal operator
    ('LE',       r'<='),                     # Less than or equal to
    ('GE',       r'>='),                     # Greater than or equal to
    ('ASSIGN',   r'='),                      # Assignment operator
    ('LT',       r'<'),                      # Less than operator
    ('GT',       r'>'),                      # Greater than operator
    ('ADD',      r'\+'),                     # Addition operator
    ('SUB',      r'-'),                      # Subtraction operator
    ('MUL',      r'\*'),                     # Multiplication operator
    ('DIV',      r'/'),                      # Division operator
    ('MOD',      r'%'),                      # Modulus operator
    ('LPAREN',   r'\('),                     # Left parenthesis
    ('RPAREN',   r'\)'),                     # Right parenthesis
    ('LBRACE',   r'\{'),                     # Left brace
    ('RBRACE',   r'\}'),                     # Right brace
    ('SEMICOLON',r';'),                      # Semicolon
    ('COMMA',    r','),                      # Comma separator
    ('DOT',      r'\.'),                     # Dot operator
    ('IDENT',    r'[A-Za-z_]\w*'),           # Identifiers
    ('MISMATCH', r'.'),                      # Any other character
]

token_regex = '|'.join('(?P<%s>%s)' % pair for pair in TOKEN_SPEC)
get_token = re.compile(token_regex).match

def tokenize(code):
    line_num = 1
    pos = 0
    tokens = []
    while pos < len(code):
        mo = get_token(code, pos)
        if mo:
            kind = mo.lastgroup
            value = mo.group(kind)
            if kind == 'NEWLINE':
                line_num += 1
            elif kind == 'SKIP' or kind == 'COMMENT':
                pass
            elif kind == 'MISMATCH':
                raise UslError(f'Unexpected character {value!r}', line_num)
            else:
                tokens.append(Token(kind, value, line_num))
            pos = mo.end()
        else:
            raise UslError(f'Unexpected character {code[pos]!r}', line_num)
    return tokens
