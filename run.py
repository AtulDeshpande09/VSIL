from lexer import tokenize
from parser import parse
from interpreter import interprete



def run(source_code):
    
    tokens = tokenize(source_code)
    ast = parse(tokens)
    interprete(ast)

if __name__ == '__main__':

    command = 'print "Hello World"'
    run(command)

