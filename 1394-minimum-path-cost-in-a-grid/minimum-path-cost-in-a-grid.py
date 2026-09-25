class Solution:
    def minPathCost(self, grid: list[list[int]], mc: list[list[int]]) -> int:
        n,m=len(grid), len(grid[0])
        dp=grid[0]
        for i in range(1,n):
            ndp=[0]*m
            for j in range(m):
                ndp[j]=grid[i][j]+min(dp[k]+mc[grid[i-1][k]][j] for k in range(m))
            dp=ndp
        return min(dp)
