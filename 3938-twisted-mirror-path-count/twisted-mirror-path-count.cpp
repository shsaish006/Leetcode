class Solution {
public:
    int uniquePaths(vector<vector<int>>& grid) {
        int n=grid[0].size() , mod=1e9+7;
        vector<array<int,2>> dp(n+1);
        dp[1]={1,1};
        for(auto &row: grid){
            for(int j=0;j<n;j++){
                int a=dp[j][0], b=dp[j+1][1];
                if(row[j]) dp[j+1]={b,a};
                else dp[j+1]={(a+b)%mod,(a+b)%mod};
            }
        }
        return dp[n][0];
        
    }
};