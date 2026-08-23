class Solution:
    def maxArea(self, nums: List[int]) -> int:
        n = len(nums); i = 0; j = n-1;
        ans = 0
        while (i<j):
            curr = (j-i)*(min(nums[i], nums[j]))
            ans = max(ans, curr)

            if(nums[i]<nums[j]): i+=1
            else: j-=1
        
        return ans
        