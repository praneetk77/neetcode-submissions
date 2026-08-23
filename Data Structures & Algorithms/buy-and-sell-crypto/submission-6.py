class Solution:

    # O(n) space and O(n) time
    def impl1(self, nums: List[int]) -> int:
        n = len(nums)
        
        ans, arr = 0, [0] * n

        for i in range(n-2, -1, -1):
            arr[i] = max(arr[i+1], nums[i+1])
        
        for i in range(n):
            ans = max(arr[i]-nums[i], ans)
        
        return ans

    def impl2(self, nums: List[int]) -> int:
        n = len(nums)
        mp = nums[n-1]
        result = 0

        for i in range(n-2, -1, -1):
            currProfit = max(0, mp - nums[i])
            result = max(result, currProfit)

            mp = max(mp, nums[i])
        
        return result

    def maxProfit(self, nums: List[int]) -> int:
        return self.impl2(nums)
        