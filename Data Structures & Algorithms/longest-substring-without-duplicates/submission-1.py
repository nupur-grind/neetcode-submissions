class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # set(), l=0, result = 0 r = in the loop
        # loop in s: loop r in set: remove r , l+=1  
        # outside (not else bc we need to exec this all time) set.add(e) result = r-l+1

        l = 0 # to track the starting of the substring
        sub = set()
        result = 0

        for r in range(len(s)):
            while s[r] in sub:
                sub.remove(s[l])
                l +=1
            sub.add(s[r])
            result = max(result,r-l+1) # track length of new long subs and we have to find the max one

        return result

        



