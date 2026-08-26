class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort
        # order to avoid duplicates, check if val == val -1, then skip whole (continue)
        # 2 pointer l and r
        # l+r, loop in num, if sum > 0 , l++, if sum<0, r--
        # end only increase l so we can find k

        res = []
        newNums = sorted(nums)

        for k,v in enumerate(newNums):
            if k >0 and v == newNums[k-1]:
                continue
            l = k+1 # basically taking k as 1 element, and then finidng other 2 with l and r.
            r = len(nums)-1
            
            while l < r :
                curSum = v + newNums[l] + newNums[r]
                if curSum > 0:
                    r -= 1
                elif curSum < 0:
                    l += 1
                else:
                    res.append([newNums[l], newNums[r], v])
                    l+=1
                    if newNums[l] == newNums[l-1]:
                        l +=1
        return res