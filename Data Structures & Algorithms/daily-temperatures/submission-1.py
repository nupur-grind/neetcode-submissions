class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stk = [i,t], res =[0]* len(t) (because default is 0 so don't need to logic the 0)
        # for in temp, while stack and t > stk[-1], stk..pop, res = i-stckI,
        #  stk.append(i,t)
        # this stack is monotonic stack because the numbers in it will always be stored in decreasing order. so we need to write it as [Temp, index] instead of [ind, temp] because we don't need ind to be the key, but need temp to be the key of decreasing order and make this a monotonic stack.

        stack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][-1]:
                popInd, popTemp = stack.pop()
                res[popInd] = i - popInd
            stack.append([i, t])
        return res





