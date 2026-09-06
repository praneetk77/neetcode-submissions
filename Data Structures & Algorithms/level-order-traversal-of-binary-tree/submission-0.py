# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root : return []
        q = []
        q.append(root)
        q2 = []
        res = []
        
        while True:
            if len(q) == 0 : break
            temp = []
            while q:
                node = q.pop(0)
                temp.append(node.val)
                if node.left : q2.append(node.left)
                if node.right : q2.append(node.right)

            res.append(temp)
            q = q2
            q2 = []

        return res
        


        