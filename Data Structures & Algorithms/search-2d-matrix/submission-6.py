class Solution:
    def searchMatrix(self, g: List[List[int]], target: int) -> bool:
        n = len(g)
        m = len(g[0])
        l = n*m

        i, j = 0, l-1
        while(i <= j):
            mid = (i+j)//2
            print(f"i is {i}, j is {j}, mid = {mid}")
            rm = mid // m
            cm = mid % m
            print(f"rm is {rm} and cm is {cm} and mid element is {g[rm][cm]}")

            if(g[rm][cm] == target):
                return True
            elif(g[rm][cm] > target):
                j = mid - 1
            else: 
                i = mid + 1
        
        return False