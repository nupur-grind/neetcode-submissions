class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) -1
        
        while l <= r:
            mid = (l + r )//2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        
        return -1

# Note: if l and r are too huge 2^31, then adding them will cause error and mid will be incorrect. so to handle that, we should use: mid = l + ((r-l) // 2)
# this will eliminate the overflow issue. 

