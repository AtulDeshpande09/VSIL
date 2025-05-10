import re

tokens = []

token_table = [         
        ('PRINT' , 'print'),
        ('STRING',r'"[^"]*"'),
        ('SKIP',r'[ \t]+'),
        ('MISMATCH' , r'.')
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

        elif kind == 'SKIP':
            continue
        elif kind == "MISMATCH":
            raise SyntaxError(f"Unexpected Character : {value}")

    return tokens

