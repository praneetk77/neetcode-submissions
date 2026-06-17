class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i,num in enumerate(nums):
            req = target - num
            if(req in map): return [map[req], i]
            else: map[num] = i
        return []
        