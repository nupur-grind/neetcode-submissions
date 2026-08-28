class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # table, row , first, last 
        # loop f<= l , 
        # if f>l, false
        # loop fir inside the row
        
        table = len(matrix)
        row = len(matrix[0])
        first = 0
        last = table - 1
        
        while first <= last:
            mid = (first + last)//2
            if target > matrix[mid][-1]:
                first  = mid +1
            elif target < matrix[mid][0]:
                last = mid -1
            else:
                break # if it is equal to target, then break this loop and proceed to next

        if first > last:
            return False

        l = 0
        r = row -1
        mid = (first + last)//2

        while l <= r:
            m = (l+r )//2
            if target > matrix[mid][m]: # matrix middle of the middle
                l = m +1 
            elif target < matrix[mid][m]:
                r = m -1
            else: 
                return True
        return False 
        
