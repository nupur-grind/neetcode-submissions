import math
class MinStack:
    
    stack = []
    minstack = []
   
    def MinStack(self, stack):
        self.stack = stack
        self.minstack = minstack

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack or val <= self.minstack[-1]:
            self.minstack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.minstack != []:
            return self.minstack[-1]
        else:
            return 0
