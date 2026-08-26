class Solution:
    def trap(self, height: List[int]) -> int:
        # maxL = 0, if l > maxL, maxL = l
        # maxR = 0, if r > maxR, maxR = r
        # water += maxL-l and += maxR-r
        # if -ve then 0 and maxL = l
        # if -ve then 0 and maxR = r
        # min(l,r), if r<l, r--, else l++


        maxL = 0
        maxR = 0
        l = 0
        r = len(height)-1
        water = 0

        while l < r:

            if maxL <=  height[l]:
                water += 0
                maxL = height[l]
            else:
                water += maxL - height[l]

            if maxR <= height[r]:
                water += 0
                maxR = height[r]
            else:
                water += maxR - height[r]

            if height[r] < height[l]:
                r -= 1
            else:
                l += 1
        return water

                
            
