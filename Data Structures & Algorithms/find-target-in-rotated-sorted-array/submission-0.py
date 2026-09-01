class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # l, r , res , m l+r//2
        # if t not in nums, return -1, break
        #l <=r, if m < r , r = m, res= m , else, l=m+1, res = m 
        # if m < t & t < r , l = m+1, target = 2
        #  t > l , m = l

        # [5,6,7,0,1,2,3]
        # [1,2,3,4,5,6]

        # l <=m -> t > m or t < l : l=m+1 else r = m-1 
        # else, t < m or t > r, r =m-1 else l = m+1

        l = 0
        r = len(nums)-1

        while l <= r:
            m = (l+r)//2
            if target == nums[m]:
                return m
                
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m+1
                else:
                    r = m-1
            else:
                if target > nums[m] or target > nums[r]:
                    r = m-1
                else:
                    l = m+1

        return -1

                





        