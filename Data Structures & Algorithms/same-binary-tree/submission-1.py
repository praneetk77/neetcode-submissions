# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def fun(curr1, curr2):
            
            if((curr1 and curr2) and (curr1.val == curr2.val)):
                return fun(curr1.left, curr2.left) and fun(curr1.right, curr2.right)
            elif((not curr1) and (not curr2)): 
                return True
            else: 
                return False
            

        return fun(p, q)


        