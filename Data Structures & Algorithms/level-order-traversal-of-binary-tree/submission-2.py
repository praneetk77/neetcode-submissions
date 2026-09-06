# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # RECURSIVE APPROACH - USING DFS and LEVEL
        res = []

        def dfs(node, level):
            if not node: return

            if(len(res)==level):
                res.append([])

            res[level].append(node.val)

            dfs(node.left, level+1)
            dfs(node.right, level+1)
        
        dfs(root, 0)
        return res
        
        # ITERATIVE APPROACH - USING QUEUE
        # if not root : return []
        # q = collections.deque([root])
        # q2 = collections.deque()
        # res = []
        
        # while True:
        #     if len(q) == 0 : break
        #     temp = []
        #     while q:
        #         node = q.popleft()
        #         temp.append(node.val)
        #         if node.left : q2.append(node.left)
        #         if node.right : q2.append(node.right)

        #     res.append(temp)
        #     q = q2
        #     q2 = deque()

        # return res
        


        