class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        result = 0

        for num in s : 
            if(num - 1 in s) : 
                continue
            
            count = 1
            while (num + 1 in s):
                num += 1
                count += 1
            
            result = max(result, count)
        
        return result
        