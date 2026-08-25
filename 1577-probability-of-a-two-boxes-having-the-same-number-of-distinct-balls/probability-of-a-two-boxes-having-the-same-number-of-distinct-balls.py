class Solution:
    def getProbability(self, balls: List[int]) -> float:
        n=sum(balls)//2 
        mx=max(balls)
        m=max(mx,2*n)
        k=len(balls)
        c=[[0]*(m+1) for _ in range(m+1)]
        for i in range(m+1):
            c[i][0]=1 
            for j in range(1,i+1):
                c[i][j]=c[i-1][j-1]+c[i-1][j]
        dp=[[0]*(2*k+1) for _ in range(n+1)]
        dp[0][k]=1 
        for b in balls:
            ndp=[[0]*(2*k+1) for _ in range(n+1)]
            for j in range(n+1):
                for d in range(2*k+1):
                    if not dp[j][d]:
                        continue 
                    for x in range(min(b,n-j)+1):
                        y=1 if x==b else (-1 if x==0 else 0)
                        ndp[j+x][d+y]+=dp[j][d]*c[b][x]
            dp=ndp 
        return dp[n][k]/c[2*n][n]