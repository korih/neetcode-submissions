class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS, COLS = len(board), len(board[0])

        for r in range(ROWS):
            row_seen = set()
            for c in range(COLS):
                cur = board[r][c]
                if cur in row_seen:
                    return False
                elif cur == ".":
                    continue
                else:
                    row_seen.add(cur)
        
        for c in range(COLS):
            col_seen = set()
            for r in range(ROWS):
                cur = board[r][c]
                if cur in col_seen:
                    return False
                elif cur == ".":
                    continue
                else:
                    col_seen.add(cur)

        for rs in range(3):
            for cs in range(3):
                sq_seen = set()
                for r in range(rs * 3, rs * 3 + 3):
                    for c in range(cs * 3, cs * 3 + 3):
                        cur = board[r][c]
                        if cur in sq_seen:
                            return False
                        elif cur == ".":
                            continue
                        else:
                            sq_seen.add(cur)

        return True

