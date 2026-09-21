class Solution {
public:
    vector<long long> resultArray(vector<int>& a, int k) {
        vector<long long> ans(k);
        int dp[5]={};
        for(int v:a){
            v%=k;
            int ndp[5]={};
            ndp[v]=1;
            for(int i=0;i<k; i++) ndp[i*v%k]+=dp[i];
            for(int i=0;i<k;i++){
                dp[i]=ndp[i];
                ans[i]+=dp[i];
            }
        }
        return ans;
        
    }
};