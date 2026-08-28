# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import numpy as np
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        cur = dummy
        p1 = list1
        p2 = list2

        while p1 and p2:
            if p1.val > p2.val:
                cur.next = ListNode(p2.val, None)
                p2 = p2.next
            else:
                cur.next = ListNode(p1.val, None)
                p1 = p1.next
            cur = cur.next
        
        while p1:
            cur.next = ListNode(p1.val, None)
            cur = cur.next
            p1.next
        while p2:
            cur.next = ListNode(p2.val, None)
            cur = cur.next
            p2 = p2.next
        
        return dummy.next

        

                



        

        





        