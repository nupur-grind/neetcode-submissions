# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # iterative DFS
        # basically as we know BST satisfies left -> node -> right, we keep checking left
        # a pointer running through left, if curr = null, cur.pop(), so the first element popped will be the left most leaf, basically the smallest, so cur.val will be the smallest one and so cur.val = n = 1 so if n = k then return cr.val
        # then go right 1 time


        curr= root 
        stack = []
        n = 0

        while curr or stack:
            while curr: 
                stack.append(curr)
                curr = curr.left
            # as it reaches null, pop the last (first leaf) and make that curr
            # and assign that as adding 1 num to n 
            curr = stack.pop()
            n +=1
            if n == k:
                return curr.val
            # if that is not true then go right and traverse through right's left tree
            curr = curr.right

            
