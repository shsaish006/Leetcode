class Solution {
public:
    double frogPosition(int n, vector<vector<int>>& e, int t, int target) {
        vector<vector<int>> g(n+1);
        for(auto &x:e){
            g[x[0]].emplace_back(x[1]);
            g[x[1]].emplace_back(x[0]);
        }
        vector<int> p(n+1), tm(n+1);
        vector<double> pr(n+1);
        queue<int> q;
        q.push(1);
        pr[1]=1;
        while(!q.empty()){
            int u=q.front(); q.pop();
            int c= g[u].size()-(u!=1);
            if(u==target)
            return tm[u]==t || c==0 ? pr[u]:0;
            if(tm[u]==t) continue;
            for(int v:g[u]){
                if(v==p[u]) continue;
                p[v]=u;
                tm[v]=tm[u]+1;
                pr[v]=pr[u]/c;
                q.push(v);
            }
        }
        return 0;
        
    }
};