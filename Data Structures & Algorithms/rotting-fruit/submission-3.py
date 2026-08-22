class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # if no rotten then we are good
        ROWS, COLS = len(grid), len(grid[0])
        rotten_fruit = deque()
        fresh_fruit = {}
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    rotten_fruit.append([r, c])
                if grid[r][c] == 1:
                    fresh_fruit[r, c] = True
            
        if len(fresh_fruit) == 0:
            return 0
        if len(rotten_fruit) == 0:
            return -1

        def bfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return 
            element = grid[r][c]
            if element == 0 or element == 2:
                return
            if fresh_fruit.get((r, c), None) != None:
                del fresh_fruit[r, c]
            rotten_fruit.append([r, c])
            grid[r][c] = 2
        
        
        sol = 0
        prev_fresh_count = len(fresh_fruit)
        while len(fresh_fruit) > 0:
            decays = len(rotten_fruit)
            i = 0
            while i < decays:
                rotten = rotten_fruit.popleft()
                bfs(rotten[0] + 1, rotten[1])
                bfs(rotten[0] - 1, rotten[1])
                bfs(rotten[0], rotten[1] + 1)
                bfs(rotten[0], rotten[1] - 1)
                i += 1

            if len(fresh_fruit) == prev_fresh_count:
                return -1
            prev_fresh_count = len(fresh_fruit)
            sol += 1
        
        return sol
            
        


