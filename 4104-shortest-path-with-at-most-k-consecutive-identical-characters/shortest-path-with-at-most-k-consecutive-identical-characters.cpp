class Solution {
public:
    int shortestPath(int n, vector<vector<int>>& edges, string labels, int k) {
        vector<vector<pair<int,int>>> g(n);
        for(auto &x:edges) g[x[0]].push_back({x[1],x[2]});
        long long inf=1e18;
        // long long inf=1e18;
        // vector<vector<long long>> d(k+1,vector<long long>(n,inf));
        // d[1][0]=0;
        vector<long long> d(n*(k+1),inf);
        auto id=[&](int u,int z){
            return u*(k+1)+z;
        };
        priority_queue<pair<long long,int>,
        vector<pair<long long,int>>, 
        greater<pair<long long,int>>>q;
        // for(int z=1;z<=k;z++){
        //     for(auto &x:edges){
        //         int u=x[0],v=x[1],w=x[2];
        //         if(d[z][u]==inf) continue;
        //         int t=labels[u]==labels[v]?z+1:1;
        //         if(t<=k) d[t][u]=min(d[t][v],d[z][u]+w);
        //     }
        // }
        d[id(0,1)]=0;
        q.push({
            0,id(0,1)
        });while(!q.empty()){
            auto[c,p]=q.top();
            q.pop();
            if(c!=d[p]) continue;
            int u=p/(k+1), z=p%(k+1);
            if(u==n-1) return c;
            for(auto [v,w]:g[u]){
                int x=labels[u]==labels[v]?z+1:1;
                if(x>k) continue;
                int np=id(v,x);
                if(c+w<d[np]){
                    d[np]=c+w;
                    q.push({
                        d[np],np
                    });
                }
            }
        }
        return -1;
    }
};