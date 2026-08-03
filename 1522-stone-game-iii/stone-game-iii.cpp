class Solution {
public:
    string stoneGameIII(vector<int>& a) {
        int n=a.size();
        vector<int> f(n,INT_MIN);
        auto dfs=[&](auto&& dfs,int i)->int{
            if(i>=n) return 0;
            if(f[i]!=INT_MIN) return f[i];
            int s=0,r=INT_MIN;
            for(int j=i;j<min(n,i+3);j++){
                s+=a[j];
                r=max(r,s-dfs(dfs,j+1));
            }
            return f[i]=r;
        };
        int r=dfs(dfs,0);
        return r==0?"Tie":r>0?"Alice":"Bob";
    }
};