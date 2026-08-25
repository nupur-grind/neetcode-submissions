class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # to count the no. of times the value occur using hashmap, write hasmap[n] = 1+ hashmap.get(n,0)  
        hashCount = {}
        freq = [[] for i in range(len(nums)+1)] #creates array with equal index as nums
        res = []

        for n in nums:
            hashCount[n] = 1 + hashCount.get(n,0) #get count of each element and pair, {key(num) : count}

        for num, cnt in hashCount.items():
            freq[cnt].append(num) # swap count as key and thus acts as index so Alice count = 2 so Alice.index = 2. So, array becomes sorted automatically ascending.
        
        for pair in range(len(freq)-1,0,-1): # loop backwards for highest count
            for num in freq[pair]:
                res.append(num)
                if len(res) == k: #if length of k is achieved, return
                    return res

        

