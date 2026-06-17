class Solution:
    def trap(self, height: List[int]) -> int:
        nums = height
        n = len(nums)
        arr1 = [0] * (n)
        arr2 = [0] * (n)

        arr1[0] = 0
        for i in range(1,n):
            arr1[i] = max(nums[i-1],arr1[i-1])
        
        arr2[n-1] = 0
        for i in range(n-2, -1, -1):
            arr2[i] = max(nums[i+1],arr2[i+1])
        
        sum = 0
        for i, num in enumerate(nums):
            sum += max(0, min(arr1[i], arr2[i]) - num)

        return sum


        