from lexer import tokenize
from parser import parse
from interpreter import interpret



def run(source_code):
    
    tokens = tokenize(source_code)
    ast = parse(tokens)
    interpret(ast)

if __name__ == '__main__':

    command = 'print "Hello World"'
    run(command)

