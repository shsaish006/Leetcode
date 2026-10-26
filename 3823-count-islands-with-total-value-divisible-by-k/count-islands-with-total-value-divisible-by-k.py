class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        from collections import deque 
        m,n=len(grid), len(grid[0])
        ans=0 
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    q=[(i,j)]
                    s=grid[i][j]
                    grid[i][j]=0
                    while q:
                        x,y=q.pop()
                        # s+=grid[x][y]
                        # grid[a][b]=0
                        for a,b in((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
                            if 0<=a <m and 0<=b<n and grid[a][b]:
                                s+=grid[a][b]
                                q.append((a,b))
                                grid[a][b]=0 
                    ans+=s%k==0 

        return ans