class Solution {
public:
    vector<int> getCoprimes(vector<int>& nums, vector<vector<int>>& edges) {
        int n=nums.size();
        vector<vector<int>> g(n);
        vector<int> ans(n,-1),id(51,-1), dep(51,-1);
        for(auto x:edges){
            g[x[0]].push_back(x[1]);
            g[x[1]].push_back(x[0]);
        }
        auto dfs=[&](auto&& dfs, int u, int p, int d)->void{
            int mx=-1;
            for(int x=1;x<=50;x++)
            if(id[x]!=-1 && __gcd(nums[u],x)==1 && dep[x]>mx){
                mx=dep[x];
                ans[u]=id[x];
            }
        
            // if(ans[u]==-1 || dep[x]> dep[nums[u]])
            // ans[u]=id[x];
            int x=nums[u], oi= id[x], od=dep[x];
            id[x]=u;
            dep[x]=d;
            for(int v:g[u])
            if(v!=p) dfs(dfs,v,u,d+1);
            id[x]=oi;
            dep[x]=od;
        };
        dfs(dfs,0,-1,0);
        return ans;
        
    }
};