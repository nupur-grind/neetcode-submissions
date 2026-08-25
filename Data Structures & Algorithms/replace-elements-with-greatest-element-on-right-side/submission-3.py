class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # arr = [1,2,3]
        # revarr = [3,3,1]
        # newarr = [3]
        maxcount = -1
        count = 0
        
        for i in range(len(arr) - 1, -1, -1):
            count = arr[i]
            arr[i] = maxcount
            maxcount = max(count,maxcount)
           
        return arr

        