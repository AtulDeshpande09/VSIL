import re

tokens = []

token_table = [         
        ('PRINT' , r'print'),
        ('STRING',r'"[^"\n]*"'),
        ('NUMBER' , r'\d+'),
        ('PLUS',r'\+'),
        ('MINUS',r'\-'),
        ('SKIP',r'[ \t]+'),
        ('NEWLINE' , r'\n')
        
               ]

token_regex = '|'.join(f'(?P<{name}>{regex})' for name, regex in token_table)


def tokenize(source_code):

    for mo in re.finditer(token_regex , source_code):

        kind = mo.lastgroup
        value = mo.group()

        if kind == 'PRINT':
            tokens.append(('PRINT',value))

        elif kind == 'STRING':
            tokens.append(('STRING',value[1:-1]))

        elif kind == "NUMBER":
            tokens.append(('NUMBER',int(value)))

        elif kind in ('PLUS','MINUS'):
            tokens.append((kind , value))
        
        elif kind == 'SKIP':
            continue

        elif kind == 'NEWLINE':
            continue

        elif kind == "MISMATCH":
            raise SyntaxError(f"Unexpected Character : {value}")

    return tokens

