class Solution:
    def climbStairs(self, n: int) -> int:
        # 1+1=2, 1+2=3, 2+3=5, 3+5=8, ... 
        # this is DFS 
        # a and b are initial elements

        a = 1
        b = 1

        for i in range(n-1):
            temp = a
            a = a+b
            b = temp
        return a



        
