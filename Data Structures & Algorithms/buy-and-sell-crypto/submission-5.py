class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        n = len(nums)
        
        ans ,arr = 0, [0] * n

        for i in range(n-2, -1, -1):
            arr[i] = max(arr[i+1], nums[i+1])
        
        for i in range(n):
            ans = max(arr[i]-nums[i], ans)
        
        return ans
        