class Solution:

    def impl1(self, board: List[List[str]]) -> bool:
        s = set()
        n = 9
        
        #check rows
        for row in board:
            # print(f"checking row : {row}")
            for cell in row:
                if(cell == "."): continue
                if(cell in s):
                    return False
                else : s.add(cell)
            s = set()

        #check cols
        for col_ind in range(n):
            # print(f"checking col_ind : {col_ind}")
            for row_ind in range(n):
                cell = board[row_ind][col_ind]
                if(cell == "."): continue
                if(cell in s):
                    return False
                else : s.add(cell)
            s = set()
        
        #check boxes
        for box_start_row_ind in range(0,n,3):
            for box_start_col_ind in range(0,n,3):
                for i in range(box_start_row_ind, box_start_row_ind+3):
                    for j in range(box_start_col_ind, box_start_col_ind+3):
                        # print(f"checking cell : {i}, {j}")
                        cell = board[i][j]
                        if(cell == "."): continue
                        if(cell in s):
                            return False
                        else : s.add(cell)
                        # print(f"set after : {s}")
                s = set()
        
        return True

        

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.impl1(board)
        