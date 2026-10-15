class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros = 0
        left = 0
        m = 0
        for i in range(len(nums)):
            if nums[i]==0:
                zeros  += 1
            if zeros > k:
                while nums[left] != 0:
                    left += 1
                zeros -= 1
                left += 1
            m = max(m, i - left + 1)

        return m