class Solution:
    def minCost(self, s: str, ec: int, fc: int) -> int:
        n=len(s)
        pre=[0]*(n+1)
        for i in range(n):
            pre[i+1]=pre[i]+int(s[i])
        def dfs(l,r):
            cnt=pre[r]-pre[l]
            lt=r-l
            if cnt==0:
                cur=fc
            else:
                cur=lt*cnt*ec 
            if lt%2:
                return cur
            m=l+lt//2 
            left=dfs(l,m)
            right=dfs(m,r)
            aadha=left+right 
            if aadha< cur:
                return aadha
            return cur 
        return dfs(0,n)