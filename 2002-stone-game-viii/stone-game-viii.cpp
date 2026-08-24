class Solution {
public:
vector<long long> p,dp;
long long dfs(int i){
    if(i==p.size()-1) return p[i];
    if(dp[i]!=LLONG_MIN) return dp[i];
    return dp[i]=max(dfs(i+1),p[i]-dfs(i+1));
}

    int stoneGameVIII(vector<int>& stones) {
        int n=stones.size();
        p.resize(n);
        dp.assign(n,LLONG_MIN);
        partial_sum(stones.begin(),stones.end(),p.begin());
        return dfs(1);
        
    }
};