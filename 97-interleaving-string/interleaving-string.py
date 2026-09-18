class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m,n=len(s1), len(s2)
        if m+n!=len(s3):
            return False 
        a=[[-1]*(n+1) for _ in range(m+1)]
        def dfs(i,j):
            if i==m and j==n:
                return True 
            if a[i][j]!=-1:
                return a[i][j]
            k=i+j 
            ok=False 
            if i<m and s1[i]==s3[k]:
                ok=dfs(i+1,j)
            if not ok and j<n and s2[j]==s3[k]:
                ok=dfs(i,j+1)
            a[i][j]=ok 
            return ok 
        return dfs(0,0)