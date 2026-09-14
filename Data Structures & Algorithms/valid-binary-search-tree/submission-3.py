# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if not root or (not root.left and not root.right): return True
        ans = [True]

        def fun(root, ans): 
            left, right = [root.val-1, root.val-1], [root.val+1, root.val+1]
            if root.left:
                left = fun(root.left, ans)
            if root.right:
                right = fun(root.right, ans)
            
            if((not(left[1]<root.val)) or (not(right[0]>root.val))): 
                # print(f"setting false at {root.val}")
                ans[0] = False
            min = left[0] if root.left else root.val
            max = right[1] if root.right else root.val

            # print(f"returning {min} and {max} for root.val = {root.val}")
            return [min,max]
        
        fun(root, ans)
        return ans[0]