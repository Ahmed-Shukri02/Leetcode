class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        quad = {(i, j): set() for i in range(3) for j in range(3)}
        row, col = [set() for i in range(9)] , [set() for i in range(9)]
        
        ROWS, COLS = len(board), len(board[0])
        for i in range(ROWS):
            for j in range(COLS):
                num, q = board[i][j], (i//3, j//3)
                if num == ".": continue
                if num in quad[q] or num in row[i] or num in col[j]:
                    
                    return False
                quad[q].add(num)
                row[i].add(num)
                col[j].add(num)
        return True
        
        def dfs(i, j):
            if (i >= ROWS):
                return True
            
            if board[i][j] != ".":
                newi, newj = i, j + 1 if j + 1 < COLS else i + 1, 0
                return dfs(newi, newj)
            
            q = (i // 3, j // 3)
            valid = False
            for num in range(10):
                if num not in quad[q] and num not in row[i] and num not in col[j]:
                    quad[q].add(num)
                    row[i].add(num)
                    col[j].add(num)
                    
                    newi, newj = i, j + 1 if j + 1 < COLS else i + 1, 0
                    if dfs(newi, newj):
                        valid = True
                    
                    quad[q].remove(num)
                    row[i].remove(num)
                    col[j].remove(num)
                    
                    if valid:
                        break
            return valid
                    