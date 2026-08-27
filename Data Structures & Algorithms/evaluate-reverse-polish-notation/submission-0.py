class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # pop prev 2 as we reach an operator
        # create variable for the popped and - or / accordingly
        # append them to stack

        stack = []

        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a = stack.pop() # last element
                b = stack.pop() # second element
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a = stack.pop() # last element
                b = stack.pop() # second element
                stack.append(int(b / a))
            else:
                stack.append(int(c))
        return stack[0]
        