# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root : return []
        q = collections.deque([root])
        level = 0
        ans = []

        while q: 
            temp = collections.deque()
            while q: 
                node = q.popleft()

                if level == len(ans): ans.append(node.val)
                else: ans[level] = node.val

                if node.left : temp.append(node.left)
                if node.right : temp.append(node.right)
            
            q = temp
            temp = []
            level += 1
            
        return ans

        # recursive
        # res = []

        # def dfs(root, level):
        #     if not root: return

        #     if level == len(res):
        #         res.append(root.val)
            
        #     dfs(root.right, level+1)
        #     dfs(root.left, level+1)
        
        # dfs(root, 0)
        # return res