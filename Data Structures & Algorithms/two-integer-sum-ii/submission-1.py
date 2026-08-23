class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        i = 0; j = n-1;

        while (i<j):
            sum = nums[i] + nums[j]

            if (sum == target): return [i+1,j+1]
            elif (sum < target): i += 1
            else: j -= 1
        
        return []

        