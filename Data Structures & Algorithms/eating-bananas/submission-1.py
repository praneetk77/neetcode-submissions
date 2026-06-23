class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i = 1; j = max(piles);
        min_ans = j

        while(i<=j):
            rate = (i+j)//2

            hours = 0
            for num in piles: hours += (num+rate-1)//rate

            if hours <= h:
                min_ans = rate
                j = rate-1
            else: 
                i = rate+1
        
        return min_ans
        