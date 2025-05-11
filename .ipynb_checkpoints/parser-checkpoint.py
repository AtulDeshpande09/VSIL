class String:
    def __init__(self,value):
        self.value = value

class Number:
    def __init__(self,value):
        self.value = value

class BinaryOp:
    def __init__(self , left , op , right ):
        self.left = left
        self.op = op
        self.right = right

class PrintStatement:
    def __init__(self,expression):
        self.expression = expression


class Parser:

    def __init__(self , tokens):
        self.tokens = tokens
        self.pos = 0
        self.no_tokens = len(tokens)

    def current(self):
        return self.tokens[self.pos] if self.no_tokens > self.pos else ("EOF",None)

    def eat(self,expected):
        if self.current()[0] == expected :
            val = self.current()[1]
            self.pos += 1
            return val
        raise SyntaxError(f"Expected {expected} but received {self.current()[0]}")

    def parse(self):
        #print('Position : ' , self.pos)
        #print("Current one : ",self.current())

        if self.current()[0] == 'PRINT':
            return self.parse_print()

        
        raise SyntaxError(f'Atleast for now I can only parse print - stay tuned for updates!!!')

    
    def parse_print(self):
        self.eat("PRINT")
        exp = self.parse_expression()
        return PrintStatement(exp)

    def parse_expression(self):
        left = self.parse_term()

        while self.current()[0] in ('PLUS','MINUS'):
            op = self.eat(self.current()[0])
            right = self.parse_term()

            left = BinaryOp(left , op , right)

        return left


    
    def parse_term(self):
        token = self.current()
        if token[0] == 'NUMBER':
            self.eat('NUMBER')
            return Number(token[1])

        elif token[0] == 'STRING':
            self.eat('STRING')
            return String(token[1])

        raise SyntaxError(f'Unexpected Token : {token}')











