# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.ans = True

        def fun(curr):
            if(not self.ans): return -1

            if(not curr): return 0

            left = fun(curr.left)
            right = fun(curr.right)

            if left-right > 1 or left-right < -1: 
                self.ans = False
                return -1
            
            return max(left, right) + 1
        
        fun(root)
        return self.ans

        