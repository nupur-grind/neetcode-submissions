class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1]* len(nums) # creating same len arr to save space later
        prefix = 1
        postfix = 1

        for i in range(len(nums)): # looping through nums
            res[i] *= prefix
            prefix *= nums[i]
        for i in range(len(nums)-1, -1, -1): # looping through nums in reverse
            res[i] *= postfix
            postfix *= nums[i]
        return res