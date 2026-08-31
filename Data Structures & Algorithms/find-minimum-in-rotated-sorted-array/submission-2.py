class Solution:
    def findMin(self, nums: List[int]) -> int:

        # l = 0, r = len(muns)-1
        # m = l+r//2, if l< m , l = m+1, m < r, res = m, r-1

        # [7, 8, 9, 0, 1, 2, 4]

        l, r = 0, len(nums)-1
        res = 0

        while l <= r :
            m = (l+r)//2

            if nums[m] < nums[r]:
                r = m
                res = nums[m]
            else:
                l = m+1
                res = nums[m]
        return res


