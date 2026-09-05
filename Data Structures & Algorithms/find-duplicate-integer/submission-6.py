class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        i,j = nums[0], nums[0]

        while(True):
            i = nums[i]
            j = nums[nums[j]]

            if(i==j): break
        
        j = nums[0]

        while(True):
            if(i==j): return i
            i = nums[i]
            j = nums[j]

            
        
        return -1
        