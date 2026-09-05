class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        i,j = 0,0

        while(True):
            i = nums[i]
            j = nums[nums[j]]

            if(i==j): break
        
        j = 0

        while(True):
            i = nums[i]
            j = nums[j]

            if(i==j): return i
        
        return -1
        