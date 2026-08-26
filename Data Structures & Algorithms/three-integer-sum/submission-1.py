class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort
        # order to avoid duplicates, check if val == val -1, then skip whole (continue)
        # 2 pointer l and r
        # l+r, loop in num, if sum > 0 , l++, if sum<0, r--
        # end only increase l so we can find k

        res = []
        nums.sort()

        for k,v in enumerate(nums):
            if k >0 and v == nums[k-1]:
                continue
            l = k+1 # basically taking k as 1 element, and then finidng other 2 with l and r.
            r = len(nums)-1
            
            while l < r :
                curSum = v + nums[l] + nums[r]
                if curSum > 0:
                    r -= 1
                elif curSum < 0:
                    l += 1
                else:
                    res.append([v,nums[l], nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l<r:
                        l +=1
        return res