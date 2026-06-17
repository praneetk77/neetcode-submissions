class Solution:
    def maxArea(self, heights: List[int]) -> int:
        nums = heights
        n = len(nums)

        ma = 0; i=0; j=n-1;

        while(i<j):
            curr_area = min(nums[i],nums[j])*(j-i)
            ma = max(curr_area, ma)

            if(nums[i] > nums[j]): j -= 1            
            elif(nums[i] < nums[j]): i += 1
            else: i += 1
        
        return ma
        