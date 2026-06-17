class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices);

        a1 = [prices[0]] * n
        a2 = [-1] * n

        for i in range(1,n):
            a1[i] = min(a1[i-1], prices[i])
        
        for i in range(n-2, -1, -1):
            a2[i] = max(a2[i+1], prices[i+1])

        print(a1)
        print(a2)

        res = 0
        for i in range(0,n-1):
            res = max(res, a2[i]-a1[i])

        return res
        