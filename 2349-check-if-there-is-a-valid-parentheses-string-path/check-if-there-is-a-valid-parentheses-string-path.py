class Solution:
    def hasValidPath(self, g: list[list[str]]) -> bool:
        m, n = len(g), len(g[0])
        if (m + n - 1) % 2 or g[0][0] == ')' or g[-1][-1] == '(':
            return False
        dp = {}
        def dfs(i, j, b):
            if i >= m or j >= n:
                return False
            b += 1 if g[i][j] == '(' else -1
            if b < 0:
                return False
            if (i, j, b) in dp:
                return dp[i, j, b]
            if i == m - 1 and j == n - 1:
                return b == 0
            dp[i, j, b] = dfs(i + 1, j, b) or dfs(i, j + 1, b)
            return dp[i, j, b]

        return dfs(0, 0, 0)