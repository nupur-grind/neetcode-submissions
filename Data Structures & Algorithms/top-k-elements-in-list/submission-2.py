class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashset = set()
        res = []
        for n in nums:
            if len(nums)<=1:
                res == nums
                break
            if n in hashset:
                if n not in res:
                    res.append(n)
            hashset.add(n)
        return res      
