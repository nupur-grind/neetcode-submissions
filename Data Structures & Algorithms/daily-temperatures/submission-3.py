class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stk = [i,t], res =[0]* len(t) (because default is 0 so don't need to logic the 0)
        # for in temp, while stack and t > stk[-1], stk..pop, res = i-stckI,
        #  stk.append(i,t)
        # this stack is monotonic stack because the numbers in it will always be stored in decreasing order.
        # I tried doing this by creating a maxtemp method and looping in reverse.
        # the structure was right but the answers in res were wrong. may be try doing that method and fix it. 
        # I think that should work too bc I saw a submission with same approach.

        stack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][-1]:
                popInd, popTemp = stack.pop()
                res[popInd] = i - popInd
            stack.append([i, t])
        return res





