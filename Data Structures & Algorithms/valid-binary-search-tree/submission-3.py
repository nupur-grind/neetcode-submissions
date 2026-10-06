# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # DFS 
        # Checking the left and right at the same time.
        # returns bool so i can return recursion bc that gives ans and checks T or F
        # as there will be not limit, we can set the bounds to [-inf, inf]
        # dfs(node,l bound, r bound), if not root: True
        # if not l < n < r : False
        # return recursion
        # return the dfs with inf bounds preset in the main

        def dfs(node, left, right):
            if not node:
                return True
            if not (left < node.val and node.val < right):
                return False
        # as all left need to be smaller than parent, right will be the parent viz node itself.
        # same in right but greater. 
        # so node bcomes n.l, l is lowest,and right is the bound viz n.val. same to right
            return (dfs(node.left, left, node.val) and dfs(node.right, node.val, right))

        return dfs(root, float("-inf"), float("inf"))

        # ##### DONT DO THESEEEE ####

        # BFS WRONG
        # q = deque, check if not root
        # while q: for i in range(q): if n = q.popleft()
        # if n.l and n.val > n.left.val: q.append(l), eif n.r: q.append(r)
        # return true.false


        # q = deque()
        # if not root:
        #     return True
        # else:
        #     q.append(root)
        
        # while q:
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         if node.left: 
        #             if node.val > node.left.val:
        #                 q.append(node.left)
        #             else:
        #                 return False
        #         elif node.right: 
        #             if node.val < node.right.val:
        #                 q.append(node.right)
        #             else:
        #                 return False
        # return True
       
        # WRONG
        # DFS
        # def dfs(node, maxVal):
        #     if not node:
        #         return True
        #     maxVal = node.val
        
        #     res = True if node.val > dfs(node.left, node.left.val) else False
        #     res = True if node.val < dfs(node.right, node.right.val) else False
        #     return res
        
        # return dfs(root,root.val)

        




        