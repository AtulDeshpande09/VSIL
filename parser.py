
def parse(tokens):
    
    if not tokens:
        raise SyntaxError("Nothing to Parse")

    token_type , value = tokens[0]

    if token_type == 'PRINT':

        if len(tokens) < 2 or tokens[1][0] != 'STRING' :
            raise SyntaxError("Expected string after print")
        return {'type':'print' , 'value':tokens[1][1]}

    raise SyntaxError(f"Unknown statement type {token_type}")


