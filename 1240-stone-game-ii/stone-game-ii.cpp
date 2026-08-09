class Solution {
public:
    int stoneGameII(vector<int>& a) {
        int n=a.size();
        vector<int> s(n+1), d(n*(n+1));
        for(int i=0;i<n;i++) s[i+1]=s[i]+a[i];
        auto dfs=[&](auto&& f, int i, int m)-> int{
            if (i+2*m>=n) return s[n]-s[i];
            int &r=d[i*(n+1)+m];
            if(r) return r;
            for(int x=1; x<=2 *m; x++)
            r=max(r,s[n]-s[i]-f(f,i+x,max(m,x)));
            return r;
        };
        return dfs(dfs,0,1);

    }
};