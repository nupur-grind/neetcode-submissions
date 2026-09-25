# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #######

        # Simplest recursive DFS
        # T: O(n), S: O(n)(worst case)

        # if not root:
        #     return 0
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        ######

        # BFS (not really a needed thing but still can do it with it)
        # T:O(n) S: O(n)
        # POPLEFT removes the first element of the deque

        # queue = deque()
        # if root:
        #     queue.append(root)
        # level = 0

        # while queue:
        #     # dont need if not root bc root already added here in BFS

        #     for i in range(len(queue)):
        #         poppedRoot = queue.popleft()
        #         if poppedRoot.left:
        #             queue.append(poppedRoot.left)
        #         if poppedRoot.right:
        #             queue.append(poppedRoot.right)
        #     level +=1
        # return level

        #######

        # Iterative DFS
        # the T and S remain same for all 

        if not root:
            return 0
        
        stack = [[root,1]]
        res = 1

        while stack:
            node, depth = stack.pop() #will remove and return its value too to use it below 

            if node: #if the removed el is not null
                res = max(depth,res)
                stack.append([node.left, depth +1]) #adds one everytime
                stack.append([node.right,depth +1])
            
        return res






 
        
 

            


        