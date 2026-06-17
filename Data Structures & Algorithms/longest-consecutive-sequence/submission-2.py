class Solution:

    def get(self, num: int, s: Set[int], mem: {}) -> int:
        if num in s: 
            mem[num] = 1 + self.get(num+1, s, mem) 
            return mem[num]
        else: 
            return 0

    def impl1(self, nums: List[int]) -> int:
        s = set()
        for num in nums: 
            if(num not in s): s.add(num)
        
        mem = {}

        max = 0
        for num in s: 
            if(num not in mem): self.get(num, s, mem)
        
        for value in mem.values():
            if(value>max): max = value
        return max
                



    def longestConsecutive(self, nums: List[int]) -> int:
        return self.impl1(nums)