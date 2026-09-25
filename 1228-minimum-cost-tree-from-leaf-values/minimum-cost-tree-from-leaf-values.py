class Solution:
    def mctFromLeafValues(self, arr: list[int]) -> int:
        n=len(arr)
        dp=[[-1]*n for _ in range(n)]
        mx=[[0]*n for _ in range(n)]
        for i in range(n):
            mx[i][i]=arr[i]
            for j in range(i+1,n):
                mx[i][j]=max(mx[i][j-1],arr[j])
        def dfs(l,r):
            if l==r:
                return 0 
            if dp[l][r]!=-1:
                return dp[l][r]
            dp[l][r]=float('inf')


            for k in range(l,r):
                dp[l][r]=min(dp[l][r],dfs(l,k)+dfs(k+1,r)+mx[l][k]*mx[k+1][r])
            return dp[l][r]
        return dfs(0,n-1)