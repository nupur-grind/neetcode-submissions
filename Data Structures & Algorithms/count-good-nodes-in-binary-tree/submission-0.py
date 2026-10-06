# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # root < x
        # node < x

        # DFS
        # USING PREORDER TRAVERSAL: means going through each node from left to right after traversing through root. 
        # create dfs with node and max, (max bc we have to keep track of ascending)
        # create res as 1 with condition if node.val >= max (always true in the first time)
        # now change the max to max of node and max.
        # now add all the left side calc values and add to the ongoing res. do the same for left.
        # return res. 
        # call the func dfs in the main func, root and root.val meaning root will be set to node and max will be root.val
        # res will not reset to 1 everytime we recurse. Every call to dfs creates its own separate local variable res. These are independent across recursive calls, even though they share the same name.

        def dfs(node, maxVal):
            if not node:
                return 0

            res = 1 if node.val >= maxVal else 0
            maxVal = max(node.val,maxVal)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)

            return res

        return dfs(root,root.val)

        

    