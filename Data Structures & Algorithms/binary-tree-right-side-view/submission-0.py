# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS
        # q = dq, root check and append root
        # res = [root]
        # whiel q : len(q) for in len :
        # popleft node, if node.l : q.append(node.l), res.append(n.l), if node.r, q.append(n.r)
        # return res

        q = deque()
        if not root:
            return []
        q.append(root)
        res = []

        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                    # if not node.right:
                        # res.append(node.left.val)

                if node.right:
                    q.append(node.right)
                    # res.append(node.right.val)
            res.append(node.val)
        return res