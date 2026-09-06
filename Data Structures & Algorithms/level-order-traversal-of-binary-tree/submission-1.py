# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root : return []
        q = deque([root])
        q2 = deque()
        res = []
        
        while True:
            if len(q) == 0 : break
            temp = []
            while q:
                node = q.popleft()
                temp.append(node.val)
                if node.left : q2.append(node.left)
                if node.right : q2.append(node.right)

            res.append(temp)
            q = q2
            q2 = deque()

        return res
        


        