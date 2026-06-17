class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        m = len(mat)
        n = len(mat[0])
        
        i = 0
        j = m*n-1

        while(i<=j):
            mid = (i+j)//2

            im, jm = divmod(mid,n)

            if(mat[im][jm] < target):
                i = mid+1
            elif(mat[im][jm] > target):
                j = mid-1
            else:
                return True
        
        return False
        