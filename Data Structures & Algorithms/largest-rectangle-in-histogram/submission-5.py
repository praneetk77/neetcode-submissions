class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        st = []
        a1 = [-1]*n; a2 = [n]*n

        for i,num in enumerate(heights):
            if(not st): 
                st.append(i)
            else: 
                while(st and num <= heights[st[-1]]):
                    st.pop()
                if(st):
                    a1[i] = st[-1]
                st.append(i)
        
        st = []

        for i in range(n-1,-1,-1):
            num = heights[i]
            if(not st): 
                st.append(i)
            else: 
                while(st and num <= heights[st[-1]]):
                    st.pop()
                if(st):
                    a2[i] = st[-1]
                st.append(i)

        res = 0
        for i in range(n):
            res = max(res, heights[i]*(a2[i]-a1[i]-1))
        return res