# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # loop
        # reverse
        # merge 

        fast, slow = head.next, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next #3 = slow.next
        prev = None 
        slow.next = None #bcause we dont need 3 but after that. so 3 space is none.

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
       
        second = prev
        first = head

        while second:
            temp = first.next
            temp2 = second.next
            # first = first.next
            first.next = second
            # second = second.next
            second.next = temp
            first = temp
            second = temp2








        