class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        i = 0; j=m*n-1;

        while(i<=j):
            mid = (i+j)//2

            row_ind = mid//n
            col_ind = mid%n

            if(matrix[row_ind][col_ind] == target):
                return True
            elif(matrix[row_ind][col_ind] < target):
                i = mid+1
            else:
                j = mid-1
        
        return False
        