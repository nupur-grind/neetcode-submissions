# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # BFS
        # q = deque, check if not root
        # while q: for i in range(q): if n = q.popleft()
        # if n.l and n.val > n.left.val: q.append(l), eif n.r: q.append(r)
        # return true.false


        q = deque()
        if not root:
            return True
        else:
            q.append(root)
        
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left: 
                    if node.val > node.left.val:
                        q.append(node.left)
                    else:
                        return False
                elif node.right: 
                    if node.val > node.right.val:
                        q.append(node.right)
                    else:
                        return False
        return True





        