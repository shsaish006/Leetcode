class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        m,n=len(grid), len(grid[0])
        def dfs(i,j):
            if i<0 or i>=m or j<0 or j>=n:
                return 0 
            if grid[i][j]:
                return 1 
            grid[i][j]=1 
            return dfs(i-1,j) & dfs(i+1,j) & dfs(i,j-1)& dfs(i,j+1)
        return sum(dfs(i,j) for i in range(m) for j in range(n) if grid[i][j]==0)
        