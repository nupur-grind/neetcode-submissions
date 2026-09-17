class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # l = 0, res, max
        # count as hashmap
        # r in s: get count[r]
        # max = (max,count[r])
        # (length of desired string - max freq of the curr letter  > k viz times allowed) if r-l+1 - max > k:
        # need to remove the l and inc it, and remove the count of l character as the string now starts from l+1
        # so, count[l]-=1, l+=1
        # res = max(r-l+1, res)


        l = 0
        res = 0
        count = {}
        maxf = 0

        for r in range(len(s)):
            count[s[r]] = 1+ count.get(s[r],0)
            maxf = max(count[s[r]],maxf)

            while ((r-l+1)-maxf) > k:
                count[s[l]] -=1
                l+=1
            res = max(r-l+1,res)
        
        return res