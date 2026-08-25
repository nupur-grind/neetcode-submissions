class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # hashset = set()
        # res = []
        # for n in nums:
        #     if len(nums)< 2:
        #         res == nums
        #         break
        #     if n in hashset:
        #         if n not in res:
        #             res.append(n)
        #             if len(res) == k:
        #                 break
        #     hashset.add(n)
        # return res
        # to count the no. of times the value occur using hashmap, write hasmap[n] = 1+ hashmap.get(n,0)  

        hashCount = {}
        freq = [[] for i in range(len(nums)+1)]
        res = []

        for n in nums:
            hashCount[n] = 1 + hashCount.get(n,0)
        for num, cnt in hashCount.items():
            freq[cnt].append(num)
        for pair in range(len(freq)-1,0,-1):
            for num in freq[pair]:
                res.append(num)
                if len(res) == k:
                    return res

        

