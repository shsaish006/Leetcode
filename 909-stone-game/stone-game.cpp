class Solution {
public:
    bool stoneGame(vector<int>& a) {
        int n=a.size();
        vector<vector<int>> f(n,vector<int>(n));
        auto dfs=[&](this auto&& dfs,int l,int r)->int{
            if(l>r)return 0;
            if(f[l][r])return f[l][r];
            return f[l][r]=max(a[l]-dfs(l+1,r),a[r]-dfs(l,r-1));
        };
        return dfs(0,n-1)>0;
    }
};