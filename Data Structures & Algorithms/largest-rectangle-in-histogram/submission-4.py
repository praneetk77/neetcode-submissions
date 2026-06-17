import collections

class Solution:
    def largestRectangleArea(self, hs: List[int]) -> int:
        stack = []
        n = len(hs)

        l2r = [(0,-1)] * n
        r2l = [(0,n)] * n

        stack.append((-1,0))

        for i, h in enumerate(hs):
            while stack and stack[-1][1] >= h and stack[-1][0] > -1 :
                stack.pop()

            l2r[i] = stack[-1]
            stack.append((i,h))
        
        stack = []
        stack.append((n,0))
        for i, h in reversed(list(enumerate(hs))):
            while stack and stack[-1][1] >= h and stack[-1][0] < n :
                stack.pop()

            r2l[i] = stack[-1]
            stack.append((i,h))

        max =0
        for i, h in enumerate(hs):
            i1, h1 = l2r[i]
            i2, h2 = r2l[i]

        for i in range(n):
            if(l2r[i][0] == -1):
                area = (r2l[i][0])*hs[i]
            else:
                area = (r2l[i][0] - l2r[i][0] - 1) *hs[i]
            if(area > max): max = area
        return max


            


        