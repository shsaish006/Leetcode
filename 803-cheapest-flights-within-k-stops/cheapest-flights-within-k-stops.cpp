class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
        int inf=1e9;
        vector<int> a(n,inf),b;
        a[src]=0;
        for(int i=0;i<=k;i++){
            b=a;
            for(auto &e:flights) if(a[e[0]]!=inf) b[e[1]]=min(b[e[1]],a[e[0]]+e[2]);
            a.swap(b);
        }
        return a[dst]==inf?-1:a[dst];
        
    }
};