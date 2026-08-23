class Solution:
    def trap(self, nums: List[int]) -> int:
        n = len(nums)
        l2r, r2l = [0] * n, [0] * n
        
        for i in range(1,n):
            l2r[i] = max(l2r[i-1], nums[i-1])
        
        for i in range(n-2, -1, -1): 
            r2l[i] = max(r2l[i+1], nums[i+1])

        # print(f"l2r is {l2r}")
        # print(f"r2l is {r2l}")
        
        ans = 0
        for i,num in enumerate(nums) : 
            hw = min(l2r[i], r2l[i])
            ans += max(0,hw-num)
        
        return ans
        