class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(len(board)):
            dupl_rows = set()
            dupl_cols = set()
            for col in range(len(board[row])):
                if board[row][col] != ".":
                    if board[row][col] in dupl_rows:
                        return False
                    dupl_rows.add(board[row][col])
                if board[col][row] != ".":
                    if board[col][row] in dupl_cols:
                        return False 
                    dupl_cols.add(board[col][row])

        dup_sq = {i: [] for i in range(9)}
        for row in range(9):
            for col in range(9):
                sq_idx = (row // 3) * 3 + (col // 3)
                if board[row][col] != ".":
                    dup_sq[sq_idx].append(board[row][col])

        for key, vals in dup_sq.items():
            if len(vals) != len(set(vals)):
                return False
        return True