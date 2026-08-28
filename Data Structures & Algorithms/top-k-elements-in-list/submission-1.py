class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashset = set()
        res = []
        if len(nums)<=1:
            res == nums
        for n in nums:
            if n in hashset:
                if n not in res:
                    res.append(n)
            hashset.add(n)
        return res      
