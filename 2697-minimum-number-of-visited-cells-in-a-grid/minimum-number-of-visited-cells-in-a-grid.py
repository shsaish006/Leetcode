class Solution:
    def minimumVisitedCells(self, g: List[List[int]]) -> int:
        from collections import deque 
        m,n=len(g),len(g[0])
        d=[[-1]*n for _ in range(m)]
        r=[list(range(n+1)) for _ in range(m)]
        c=[list(range(m+1)) for _ in range(n)]
        def f(a,x):
            while a[x]!=x:
                a[x]=a[a[x]]
                x=a[x]
            return x 
        q=deque([(0,0)])
        d[0][0]=1 
        r[0][0]=1 
        c[0][0]=1
        # d[0][0]=1 
        while q:
            i,j=q.popleft()
            z=d[i][j]+1 
            x=f(r[i],j+1)
            while x<n and x<=j+g[i][j]:
                d[i][x]= z 
                r[i][x]=f(r[i],x+1)
                c[x][i]=f(c[x],i+1)
                q.append((i,x))
                x=f(r[i],x)
            x=f(c[j],i+1) 
            while x<m and x<=i+g[i][j]:
                d[x][j]=z 
                c[j][x]=f(c[j],x+1)
                r[x][j]=f(r[x],j+1)
                q.append((x,j))
                x=f(c[j],x)
        return d[-1][-1]
        