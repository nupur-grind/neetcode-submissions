# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

    

        prev = None
        curr = head
        # (1,2,3,4)
        
        while curr:
            nxt = curr.next  #  2 3 4 1
            curr.next = prev  # n 1 2 3
            prev = curr      #  1 2 3 4
            curr = nxt       #  2 3 4 1
            
        return prev 
            


        