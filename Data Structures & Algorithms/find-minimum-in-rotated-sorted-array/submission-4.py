class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums); i = 0; j = n-1;

        if(n==1): return nums[0]
        elif(n==2): return min(nums)
        elif(nums[0]<nums[n-1]): return nums[0]


        while(i<j):
            mid = (i+j)//2

            if(nums[mid] > nums[mid-1] and nums[mid]<nums[mid+1]):
                if(nums[mid]>nums[i]):
                    i = mid+1
                else: 
                    j = mid-1
            elif(nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]):
                return nums[mid+1]
            else: 
                return nums[mid]
        
        return 0




