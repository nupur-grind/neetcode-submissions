# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        # if both smaller than the curr, curr.left
        # if both bigger than the curr, curr.right
        # if 1 is smaller/bigger, meaning either they have an anscester or it is the node itself. either way it is the curr that is the answer so return curr

        curr = root

        while curr: 
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr. left
            else:
                return curr
