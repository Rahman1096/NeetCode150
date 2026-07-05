class MinStack:

    def __init__(self):
        self.main_stack=[]
        self.min_stack=[]


    def push(self, value: int) -> None:
        #Push the minimum value so far based on condition
        if not self.min_stack:
            self.min_stack.append(value)
        else:
            self.min_stack.append(min(value,self.min_stack[-1]))

        #VALUE WILL BE PUSHED ONTO MAIN STACK UNCONDITIONALY    
        self.main_stack.append(value)

    def pop(self) -> None:
            self.main_stack.pop()   
            self.min_stack.pop() 

    def top(self) -> int:
        return self.main_stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        