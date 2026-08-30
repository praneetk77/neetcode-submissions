class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        i,j = 0, n-1

        result = float('inf')

        while(i <= j):
            mid = (i+j)//2

            result = min(result, nums[mid])

            # mid is in the second upward slope
            if(nums[mid] < nums[j]):
                # check left side 
                j = mid - 1
            # mid is in the first upward slope
            else:
                # check right side
                i = mid+1
        
        return result

