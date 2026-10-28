class Solution:
    def minCost(self, grid):
        m, n = len(grid), len(grid[0])
        mx = max(max(row) for row in grid)
        mx = 1 << mx.bit_length()
        f = [[[0] * mx for _ in range(n)] for _ in range(m)]
        f[0][0][grid[0][0]] = 1
        for i in range(m):
            for j in range(n):
                x = grid[i][j]

                if i > 0 or j > 0:
                    for k in range(mx):
                        if i > 0 and f[i - 1][j][k ^ x]:
                            f[i][j][k] = 1
                        if j > 0 and f[i][j - 1][k ^ x]:
                            f[i][j][k] = 1

        for k in range(mx):
            if f[m - 1][n - 1][k]:
                return k