class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        from collections import defaultdict 
        g=defaultdict(list)
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        ans=[0]*n 
        sz=[1]*n 
        def dfs(a,p,d):
            ans[0]+=d 
            for b in g[a]:
                if b!=p:
                    dfs(b,a,d+1)
                    sz[a]+=sz[b]
        def dfs2(a,p):
            for b in g[a]:
                if b!= p:
                    ans[b]=ans[a]-sz[b]+n-sz[b]
                    dfs2(b,a)
        dfs(0,-1,0)
        dfs2(0,-1)
        return ans
        