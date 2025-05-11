from lexer import tokenize
from parser import Parser
from interpreter import Interpreter

with open('test.vsil') as f:
    code = f.read()

tokens = tokenize(code)
parser = Parser(tokens)
ast = parser.parse()
interpreter = Interpreter()
interpreter.eval(ast)
