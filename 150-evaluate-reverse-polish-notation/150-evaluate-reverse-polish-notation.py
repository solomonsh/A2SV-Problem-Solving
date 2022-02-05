class Solution:
    
    def calculate(self,val1,val2,operator):
        
        if operator == "+": return val1+val2
        elif operator == '-': return val2-val1
        elif operator == "*": return val1*val2
        elif operator == "/": return int(val2/val1)
    
    def evalRPN(self, tokens):
        
        operators = ['+','-','*','/']
        
        stack = []
        
        for token in tokens:
            if len(stack) == 0:
                stack.append(token)
                
            else:
                if token not in operators:
                    stack.append(token)
                
                else:
                    if len(stack)>=2:
                        val1 = stack.pop()
                        val2 = stack.pop()

                        result  = self.calculate(int(val1),int(val2),token)
                  
                        stack.append(result)
                
        return stack[-1]
        
