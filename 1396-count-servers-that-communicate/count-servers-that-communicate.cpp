class Solution {
public:
    int countServers(vector<vector<int>>& grid) {
        int m=grid.size(), n=grid[0].size(),ans=0;
        vector<vector<int>> v(m, vector<int>(n));
        auto dfs=[&](auto&& dfs, int i ,int j)->int{
            if(i<0 || i>=m || j<0 || j>=n || !grid[i][j]|| v[i][j]) return 0;
            v[i][j]=1;
            int x=1;
            // x+=dfs(dfs,i+1,j);
            // x+=dfs(dfs,i-1,j);
            // x+=dfs(dfs,i,j+1);
            // x+=dfs(dfs,i,j-1);
            for(int k=0;k<n;k++) if(grid[i][k]) x+=dfs(dfs,i,k);
            for(int k=0;k<m;k++) if(grid[k][j]) x+=dfs(dfs,k,j);
            return x;
        };
        for(int i=0;i<m;i++)
        for(int j=0;j<n;j++)
        if(grid[i][j]&& !v[i][j]){
            int x=dfs(dfs,i,j);
            if(x>1) ans+=x;
        }
        return ans;
    }
};