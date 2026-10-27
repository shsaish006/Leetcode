class Solution:
    def createGrid(self, m, n):
        
        g = [['#'] * n for _ in range(m)]
        g[0] = ['.'] * n
        for i in range(m):
            g[i][n - 1] = '.'
        return [''.join(row) for row in g]