class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #sorting and all will take much longer, we need to do this in linear time.
        numSet = set(nums) # set removes all duplicates from the array
        maxlength = 0
        # length = 0

        for n in numSet:
            if (n-1) not in numSet:
                length = 1
                while (n+length) in numSet:
                    length += 1
                maxlength = max(length,maxlength) #max covers edge case of [0] (just 1 element)
        
        return maxlength

