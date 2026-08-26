class Solution:
    def isPalindrome(self, s: str) -> bool:

        # This method takes O(n) space and not good for interviewas, but just in case to understand.
        # newS = ''
        # for c in s:
        #     if c.isalnum():
        #         newS += c.lower()
            
        # return newS == newS[::-1]

        # This is the real method of 2 pointers  
        l = 0
        r = len(s)-1

        while l < r:
            while l<r and not self.isAlphaNum(s[l]):
                l += 1
            while r > l and not self.isAlphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    def isAlphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))


