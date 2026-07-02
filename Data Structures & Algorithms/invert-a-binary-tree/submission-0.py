# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def fun(self, root: Optional[TreeNode]):
        if not root : return

        temp = root.left
        root.left = root.right
        root.right = temp

        self.fun(root.left)
        self.fun(root.right)
    
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.fun(root)
        return root