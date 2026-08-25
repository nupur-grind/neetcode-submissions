# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import numpy as np
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list2:
            return list1
        if not list1:
            return list2
            
        dummy = ListNode(0, None)
        cur = dummy

        while list1 and list2:
            if list1.val > list2.val:
                cur.next = ListNode(list2.val, None)
                list2 = list2.next
            else:
                cur.next = ListNode(list1.val, None)
                list1 = list1.next
            cur = cur.next

        if list1:
            cur.next = list1
        if list2:
            cur.next = list2
        
        return dummy.next

        

                



        

        





        