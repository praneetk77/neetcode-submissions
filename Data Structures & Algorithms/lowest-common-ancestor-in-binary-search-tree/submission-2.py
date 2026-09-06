# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def check(self, root: TreeNode, p: TreeNode, q: TreeNode, ans: List[TreeNode]) -> List[bool]:
        res = False, False
        if not root : return res
        
        if root.val == p.val :
            res = True, self.check(root.left, p, q, ans)[1] or self.check(root.right, p, q, ans)[1]

        elif root.val == q.val : 
            res = self.check(root.left, p, q, ans)[0] or self.check(root.right, p, q, ans)[0], True

        else :
            left_res = self.check(root.left, p, q, ans)
            right_res = self.check(root.right, p, q, ans)
            res = left_res[0] or right_res[0], left_res[1] or right_res[1]

        # print(f"for root = {root.val}    ; res = {res}")
        if res == (True, True) : 
            print("appending")
            ans.append(root)
        return res

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ans = []

        self.check(root, p, q, ans)
        # print(f"size of ans = {len(ans)} and value of first : {ans[0].val}")
        return ans[0]
        

        
