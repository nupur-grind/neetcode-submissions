class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
      # sort arr , while l <=r
      # m= l+r//2, for i in plies, res += math.ceil(i / m), if res < h, r = m-1 , el res > h , l= mid+1
      # return m 

      l = 1
      r = max(piles)
      res = r
      

      while l <= r :
        k = (l+r)//2
        hours = 0 # initialize here bc it needs to be 0 everytime new pile loop.
        for i in piles:
          hours += math.ceil(i/k)
          
        if hours <= h:
          res = min(res,k)
          r = k-1
        else:
          l = k+1
      return res
