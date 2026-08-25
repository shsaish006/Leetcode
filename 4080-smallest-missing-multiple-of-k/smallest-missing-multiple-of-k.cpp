class Solution {
public:
    int missingMultiple(vector<int>& nums, int k) {
        int n=nums.size();
        vector<bool> dp(n*k+k);
        for(int x:nums)
        if(x<dp.size())  dp[x]=1;
        for(int i=k ;; i+=k) if(!dp[i]) return i;
        
    }
};