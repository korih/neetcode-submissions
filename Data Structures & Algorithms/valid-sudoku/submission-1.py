class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 3 checks, one for row, col, and square
        # row is easy
        # col is looking at list list
        # square is list list but only a few cells
        # n rows, n col, n/3 squares

        # check rows
        for y in board:
            seen = {}
            for x in y:
                if x in seen:
                    return False
                elif x == '.':
                    continue
                else:
                    seen[x] = x

        for x in range(0, 9):
            seen = {}
            for y in range(0,9):
                val = board[y][x]
                if val in seen:
                    return False
                elif val == '.':
                    continue
                else:
                    seen[val] = val
        
        for i in range(0, 3):
            for j in range(0,3):
                seen = {}
                row = i * 3
                col = j * 3
                for y in range(row, row+3):
                    for x in range(col, col+3):
                        val = board[y][x]
                        if val in seen:
                            return False
                        elif val == '.':
                            continue
                        else:
                            seen[val] = val

        return True
