class Solution {
public:
    vector<vector<int>> highestPeak(vector<vector<int>>& isWater) {
        int m=isWater.size(), n=isWater[0].size(), x=1e9;
        vector<vector<int>> dp(m,vector<int>(n,x));
        for(int i=0;i<m;i++) for(int j=0;j<n;j++)
        if(isWater[i][j]) dp[i][j]=0;
        for(int i=0;i<m;i++)
        for(int j=0;j<n;j++){
            if(i) dp[i][j]=min(dp[i][j],dp[i-1][j]+1);
            if(j) dp[i][j]=min(dp[i][j],dp[i][j-1]+1);
        }
        for(int i=m-1;i>=0;i--)
        for(int j=n-1;j>=0;j--){
            if(i<m-1) dp[i][j]=min(dp[i][j],dp[i+1][j]+1);
            if(j<n-1) dp[i][j]=min(dp[i][j], dp[i][j+1]+1);
        }
        return dp;
    }
};