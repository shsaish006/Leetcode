class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n=len(intervals)
        a=sorted(range(n),key=lambda i:intervals[i][1])
        b=[intervals[i][1] for i in a]
        dp=[(0,[])]*(n+1)
        for k in range(4):
            ndp=[(0,[])]*(n+1)
            for i in range(1,n+1):
                j=bisect_left(b,intervals[a[i-1]][0])
                x=dp[j]
                y=(x[0]-intervals[a[i-1]][2],sorted(x[1]+[a[i-1]]))
                ndp[i]=min(y,ndp[i-1])
            dp=ndp 
        return dp[n][1]
        

        