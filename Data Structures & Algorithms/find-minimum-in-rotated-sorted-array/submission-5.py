class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        i,j = 0, n-1

        result = float('inf')

        while(i <= j):
            mid = (i+j)//2

            if(nums[mid] < nums[j]):
                if(nums[mid] < nums[i]):
                    result = min(result, nums[mid])
                    j = mid - 1
                else:
                    result = min(result, nums[mid])
                    j = mid - 1
            else:
                result = min(result, nums[mid])
                i = mid+1
        
        return result

