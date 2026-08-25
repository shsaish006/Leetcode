class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n=len(vals)
        p=list(range(n))
        g=[[] for _ in range(n)]
        c=[{} for _ in range(n)]
        def f(x):
            while x!=p[x]:
                p[x]=p[p[x]]
                x=p[x]
            return x 
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        for i in range(n):
            c[i][vals[i]]=1 
        ans=n 
        for v,a in sorted((vals[i],i ) for i in range(n)):
            for b in g[a]:
                if vals[b]>v:
                    continue 
                x,y=f(a),f(b)
                if x==y:
                    continue 
                ans+=c[x].get(v,0)*c[y].get(v,0)
                p[x]=y 
                c[y][v]=c[y].get(v,0)+c[x].get(v,0)
        return ans
        