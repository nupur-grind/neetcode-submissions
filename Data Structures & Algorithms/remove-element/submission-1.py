from collections import Counter
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #nums : k and val
        #nums: first k then val
        #expectedNums = []
        #unexpectedNums = []
        #nums.remove(val)
        temp = 0
        

        for i in range(len(nums)-1):
            if nums[i] != val:
                #temp = num[i]
                #nums.remove(nums[i])
                nums[temp] = nums[i]
                temp+=1
                #expectedNums.append(i)
                #expectedNums.sort() 
            
        # expectedNums = expectedNums.sort()
        # k = expectedNums.count()
        #k = len(nums)
        

        print("valid ",nums)
        print("k ",temp)
        return temp