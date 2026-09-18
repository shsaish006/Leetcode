class Solution {
public:
    int minCost(int mt, vector<vector<int>>& ed, vector<int>& pf) {
        int n=pf.size(), inf=1e9;
        vector<vector<int>> dp(mt+1,vector<int>(n,inf));
        dp[0][0]=pf[0];
        // vector<int> dp(n,inf), ndp(n);
        // dp[0]=pf[0];
        // int ans=inf;
        for(int i=0;i<=mt;i++){
            // ndp=dp;
            for(auto &e:ed){
                int u=e[0], v=e[1], w=e[2];
                if(i+w>mt) continue;
                if(dp[i][u]!=inf) dp[i+w][v]=min(dp[i+w][v],dp[i][u]+pf[v]);
                // ndp[v]=min(ndp[v],dp[u]+pf[v]);
                if(dp[i][v]!=inf) dp[i+w][u]=min(dp[i+w][u], dp[i][v]+pf[u]);
                // ndp[u]=min(ndp[u],dp[v]+pf[u]);
            }
            // dp.swap(ndp);
            // ans=min(ans,dp[n-1]);
        }
        int ans=inf;
        for(int i=0;i<=mt;i++) ans=min(ans,dp[i][n-1]);
        return ans ==inf ?-1:ans;
        
    }
};