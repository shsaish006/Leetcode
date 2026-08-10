class Solution {
public:
    bool winnerSquareGame(int n) {
        vector<int> f(n+1,-1);
        auto dfs= [&](this auto&& dfs, int n)->bool {
            if(n<0) return 0;
            if(f[n]!= -1) return f[n];
            for(int i=1;i*i<=n;i++)
            if(!dfs(n-i*i)) return f[n]=1;
            return f[n]=0;
        };
        return dfs(n);
        
    }
};