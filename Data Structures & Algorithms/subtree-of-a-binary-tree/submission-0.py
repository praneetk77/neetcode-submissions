# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   

    def check(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if(root is None and subRoot is None): return True
        elif(root is None or subRoot is None): return False

        if(root.val == subRoot.val):
            return self.check(root.left, subRoot.left) and self.check(root.right, subRoot.right)

        else: return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if(root is None and subRoot is None): return True
        elif(root is None or subRoot is None): return False

        if self.check(root, subRoot): return True
        else: return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)







        