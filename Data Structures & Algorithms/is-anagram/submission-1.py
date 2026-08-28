class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        set1 = set()
        for i in s:
            set1.add(i)

        set2 = set()
        for j in t:
            set2.add(j)
        
        if set2 == set1:
            return True
        else:
            return False