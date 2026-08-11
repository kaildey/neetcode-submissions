class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        ROWS, COLS = len(grid), len(grid[0])

        def helper(i, j):
            if i < 0 or i >= ROWS:
                return
            if j < 0 or j >= COLS:
                return
            if grid[i][j] != '1':
                return

            grid[i][j] = '2'
            helper(i-1, j)
            helper(i, j+1)
            helper(i+1, j)
            helper(i, j-1)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == '1':
                    helper(i, j)
                    count += 1
        
        return count