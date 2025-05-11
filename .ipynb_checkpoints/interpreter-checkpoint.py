from parser import Number , String , BinaryOp , PrintStatement

class Interpreter:

    def eval(self,node):
        
        if isinstance(node,Number):
            return node.value
        
        elif isinstance(node,String):
            return node.value
        
        elif isinstance(node,PrintStatement):
            value = self.eval(node.expression)
            print(value)
        
        elif isinstance(node,BinaryOp):
            left = self.eval(node.left)
            right = self.eval(node.right)

            if node.op == '+':
                return left+right
            elif node.op =='-':
                return left-right
            elif node.op =='*':
                return left*right
            elif node.op =='/':
                return left//right



