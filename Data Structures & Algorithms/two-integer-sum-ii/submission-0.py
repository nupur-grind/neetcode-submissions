class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 2 pointers
        # l+r if bigger, r--, if smaller, l++
        # if == target, res.append(l,r)

        l = 0
        r = len(numbers) -1
        res = []

        while l<r:
            add = numbers[l] + numbers[r]
            if add > target:
                r -= 1
            if add < target:
                l += 1
            if add == target:
                res.append(numbers[l])
                res.append(numbers[r])
                return list(res)
           
    
        

