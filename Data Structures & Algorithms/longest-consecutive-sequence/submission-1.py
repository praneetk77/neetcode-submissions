class Solution:

    def get(self, num: int, map: {}, mem: {}) -> int:
        if num in map.keys(): 
            mem[num] = 1 + self.get(num+1, map, mem) 
            return mem[num]
        else: 
            return 0

    def impl1(self, nums: List[int]) -> int:
        map = {}
        for num in nums: 
            if(num not in map): map[num] = False
        
        mem = {}

        max = 0
        for num,is_visited in map.items(): 
            if(num not in mem): self.get(num, map, mem)
        
        for value in mem.values():
            if(value>max): max = value
        return max
                



    def longestConsecutive(self, nums: List[int]) -> int:
        return self.impl1(nums)