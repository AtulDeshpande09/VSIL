
def interprete(ast):

    if ast['type'] == 'print':
        print(ast['value'])
    else :
        raise RuntimeError(f"Unknown Statement : {ast['type']}")
