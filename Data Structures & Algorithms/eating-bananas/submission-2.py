class Solution:
    def minEatingSpeed(self, nums: List[int], h: int) -> int:
        m = 0
        for num in nums: m = max(num, m)

        i, j = 1, m
        result = -1

        while (i<=j):
            mid = (i+j)//2

            hours = 0
            for num in nums: hours += (num + mid - 1) // mid

            if(hours <= h):
                result = mid
                j = mid-1
            elif(hours > h):
                i = mid+1
            
        return result
        