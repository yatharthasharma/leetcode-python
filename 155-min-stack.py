class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum_stack = []
        

    def push(self, val: int) -> None:
        if self.getMin() >= val:
            self.minimum_stack.append(val)
        self.stack.append(val)
        

    def pop(self) -> None:
        if self.minimum_stack[-1] == self.stack[-1]:
            self.minimum_stack.pop()
        self.stack.pop()
        

    def top(self) -> int:
        if(len(self.stack) == 0):
            return 2**31
        return self.stack[-1]

    def getMin(self) -> int:
        if(len(self.minimum_stack) == 0):
            return 2**31;
        return self.minimum_stack[-1]
        


stack = MinStack()
stack.push(-2)
stack.push(0)
stack.push(-1)
stack.getMin() # -1
print(stack.top())
print(stack.pop())
print(stack.getMin())