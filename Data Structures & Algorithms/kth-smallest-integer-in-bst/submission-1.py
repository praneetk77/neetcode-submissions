# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        map = {}

        def fun(root):
            if not root: return 0

            left = fun(root.left)
            right = fun(root.right)

            ans = 1 + left + right

            map[root] = ans
            return ans
        
        temp = root
        fun(temp)
        
        # for key, value in map.items():
        #     print(f"key : {key.val} and val : {value}")

        def find(node, k):
            
            lc = 0
            if node.left: lc = map[node.left]

            if(lc!=0 and k<=lc):
                # go left
                return find(node.left, k)
            else:
                newk = k-lc
                if newk == 1 : return node.val
                else: 
                    return find(node.right, newk-1)
        
        return find(root, k)

        