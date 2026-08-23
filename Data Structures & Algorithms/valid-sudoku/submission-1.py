class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        size = 9
        col_map = [[False]*(size+1) for _ in range(size)]
        row_map = [[False]*(size+1) for _ in range(size)]
        square_map = [[False]*(size+1) for _ in range(size)]

        for r in range(size):
            for c in range(size):
                if board[r][c] == "." : 
                    continue
                
                num = int(board[r][c])
                sq_index = (r // 3) * 3 + (c // 3)

                if(col_map[c][num] or row_map[r][num] or square_map[sq_index][num]): 
                    return False
                
                col_map[c][num] = True
                row_map[r][num] = True
                square_map[sq_index][num] = True
        
        return True
        