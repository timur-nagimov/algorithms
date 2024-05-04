class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            if i >= len(grid) or j >= len(grid[0]):
                return
            if i < 0 or j < 0:
                return
            if grid[i][j] != '1':
                return

            grid[i][j] = '0'
            dfs(i, j+1)
            dfs(i, j-1)
            dfs(i+1, j)
            dfs(i-1, j)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)

        return count
