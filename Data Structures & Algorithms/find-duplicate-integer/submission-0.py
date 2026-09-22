class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # linked list and linked loop so need to find the start of the loop
        # if need to find loop t/f, 2 pointers, if need to find start of loop 3 pointers
        # since this is arr we write accordingly. using this bc S: O(1)
        
        # fast, slow = 0
        # loop, slow = n[s] and fast = n[n[f]], if f==s, break
        # slow2 = 0, right now slow has value but slow2 is at 0
        # loop,slow = n[s], slow2 = n[s2], if s == s2, break return s


        fast, slow = 0,0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if fast == slow:
                break
        
        slow2  = 0

        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow == slow2:
                break
        return slow

        