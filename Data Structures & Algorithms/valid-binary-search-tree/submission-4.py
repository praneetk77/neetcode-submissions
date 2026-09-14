# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def fun(node, left, right):
            if not node: return True

            if(node.val <= left or node.val >= right):
                return False

            return fun(node.left, left, node.val) and fun(node.right, node.val, right)

        return fun(root, float('-inf'), float('inf'))