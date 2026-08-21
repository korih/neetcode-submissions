class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        sol = 0

        def dfs(x, y):
            if x < 0 or y < 0:
                return 0
            if x >= len(grid[0]) or y >= len(grid):
                return 0
            if grid[y][x] == 0:
                return 0
            
            grid[y][x] = 0
            left = dfs(x - 1, y)
            right = dfs(x + 1, y)
            up = dfs(x, y + 1)
            down = dfs(x, y - 1)
            return left + right + up + down + 1

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 1:
                    sol = max(dfs(x, y), sol)
        
        return sol