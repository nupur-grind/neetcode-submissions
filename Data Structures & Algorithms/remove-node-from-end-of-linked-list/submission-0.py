# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # dummy and left are 0
        # right = n -> while n>0 and right(notnull), r = r.next, n-=1
        # loop though, while right: l.next, r.next
        # jump left to 1 more, l.nex = l.nex.nex
        # everything is attached to dummy viz attached to head, so dummy.nex

        dum = ListNode(0,head)
        left = dum
        right = head

        while n >0 and right:
            right = right.next
            n-=1
        
        while right: 
        #and right.next: not including because gave (1,3,4).here,r is 3 before loop and after running once, r.nex becomes null and then it won't run, leaving l as 1, then l.nex = l.nex.nex skips 2 instead of 3. 
            left = left.next
            right = right.next
        left.next = left.next.next

        return dum.next



        
       
        
            
                
        
        