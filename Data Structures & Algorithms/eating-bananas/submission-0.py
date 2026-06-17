class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # upper bound for k = max piles[i]
        # lower bound for k = 1

        i=1 
        j= sum(piles)

        ans = j
        while (i<=j):
            mid = (i+j) // 2

            s = 0
            for pile in piles: 
                s += math.ceil(pile/mid)
            
            if(s<=h):
                ans = mid
                j = mid-1
            else:
                i = mid+1
        
        return ans
        