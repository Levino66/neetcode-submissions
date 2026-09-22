class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            row = set()
            col = set()
            box = set()
            for j in range(9):
                elrow = board[i][j]
                if elrow.isnumeric():
                    if elrow in row:
                        return False
                    else:
                        row.add(elrow)
                
                elcol = board[j][i]
                if elcol.isnumeric():
                    if elcol in col:
                        return False
                    else:
                        col.add(elcol)
                
                elbox = board[i//3*3 + j//3][i%3*3 + j%3]
                if elbox.isnumeric():

                    if elbox in box:
                        return False
                    else:
                        box.add(elbox)
        return True
                

                
                    
                


        