# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0

        def fun(node, max):
            if not node : return 0

            if node.val >= max:
                newmax = node.val
                return 1 + fun(node.left, newmax) + fun(node.right, newmax)
            else:
                return fun(node.left, max) + fun(node.right, max)
        
        return fun(root, root.val)
        