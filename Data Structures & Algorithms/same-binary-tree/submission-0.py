# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if no right or noleft : false
        # if n.left < n < n.right: true else false
        
         # T: O(n), S: O(n)(worst case)

        if (p and not q) or (q and not p):
            return False
        if not q and not p:
            return True
        if p.val != q.val:
            return False
        
        l = self.isSameTree(p.left, q.left)
        r = self.isSameTree(p.right, q.right)

        if l and r:
            return True
        else:
            return False


