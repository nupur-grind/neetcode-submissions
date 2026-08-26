class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #  2 pointer l and r
        #  maxA = 0, w = r - l , h = min(l,r), so A = w * h, if A > maxA, maxA = A
        #  if arr[l] < arr[r], l++, else r ++
        
        l = 0
        r = len(heights)-1
        maxA = 0

        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            area = width * height

            if area > maxA and l<r:
                maxA = area
            if heights[l] < heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        return maxA