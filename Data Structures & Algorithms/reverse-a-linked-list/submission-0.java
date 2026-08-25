/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {

    ListNode prev;
    ListNode tempNext;
    ListNode curr;
    public ListNode reverseList(ListNode head) {
        curr = head;
        while (curr != null){
            //(0,1,2,3)
            // curr =0,1,2,3
        ListNode nextTemp = curr.next; //t=1,2,3,nl
        curr.next = prev; //cn=nul,0,1,2
        prev = curr; //p=0,1,2,3
        curr = nextTemp; //c=1,2,3,null


            // curr.next = tempNext;
            // curr.next = prev;
        }
        return prev;
    }
}
