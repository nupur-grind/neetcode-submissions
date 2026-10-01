# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS
        # T: O(n), S: O(n)
        # res[]
        # deque
        # if not root check, dq.append(root)
        # while q: len = q len, level = [] (bc we need only for for loop)
        # popleft, if node , levle.append(node), append[n.l], ap[r.l]
        # if level, res.append, return res


        # FOR THE FOR LOOP
        # first root : q len = 1 so exec 1 time, pop, append and stop, then level
        # while: now q len = 2 (l and r), so exec 2 time, pop, append and stop, then level,
        # while: now q len = 4 (leaves), so exec 4 time, only pop, bc null l r so stop then level


        res = []
        q = deque()
        if not root:
            return []
        
        q.append(root)

        while q:
            l = len(q)
            sublist = []

            for i in range(l):
                node = q.popleft()
                sublist.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if sublist:
                res.append(sublist)
        
        return res
                

