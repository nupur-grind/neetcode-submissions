class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # l > r , p = r-l, max(p)
        # max = 0, l =0, r = l+1, p = r-l, if max < p, max=p, r ++, else l++,r++
        # l constant > while arr-l: p = r-l, if max < p, max=p. r ++

        l = 0
        r = 1
        maxp = 0

        while r < len(prices):
            profit = prices[r] - prices[l]

            if profit > maxp:
                for i in range(l+1,len(prices)):
                    profit = prices[i] - prices[l]
                    if maxp < profit:
                        maxp = profit
                    i +=1
                r+=1

            else:
                l +=1
                r +=1
            
        return 0 if profit <= 0 else maxp

        

        