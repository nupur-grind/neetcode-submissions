class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 2 pointers
        # l+r if bigger, r--, if smaller, l++
        # if == target, res.append(l,r)

        l = 1
        r = len(numbers)
        res = []

        while l<r:
            add = numbers[l-1] + numbers[r-1]
            if add > target:
                r -= 1
            if add < target:
                l += 1
            if add == target:
                res.append(l)
                res.append(r)
                return list(res)
           
    
        

