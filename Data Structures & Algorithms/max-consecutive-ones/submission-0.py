import math
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxcount = 0
        count = 0
        mylist = []


        for i in nums:
            if i == 1:
                count += 1
                if maxcount < count:
                    maxcount = count
                    mylist.append(maxcount)
            if i == 0:
                count = 0 

        print(mylist)
        maxoutput = max(mylist)  


        return maxoutput
            
        