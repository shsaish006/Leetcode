class Solution {
public:
    vector<int> remainingMethods(int n, int k, vector<vector<int>>& in) {
        vector<vector<int>> a(n);
        vector<int> s(n), ans;
        for(vector<int> e: in)
        a[e[0]].push_back(e[1]);
        auto dfs=[&](auto&& dfs, int x)->void{
            s[x]=1;
            for(int y: a[x])
            if(!s[y])
            dfs(dfs,y);
        };
        dfs(dfs,k);
        for(vector<int> e: in){
            if(!s[e[0]]&&s[e[1]]){
                for(int i=0;i<n;i++)
                ans.push_back(i);
            return ans;
            }
        }
        // for(auto e:in){
        //     if(!s[e[0]]&& s[e[1]]){
        //         for(int i=0;i<n;i++)
        //         if(!s[i])
        //         ans.push_back(i);
        //     return ans;
        //     }
        // }
        for(int i=0;i<n;i++)
        if(!s[i])
        ans.push_back(i);
        return ans;
        
    }
};