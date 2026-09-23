class Solution {
public:
    int minOperations(vector<int>& nums, int x) {
        int n=nums.size();
        int s=accumulate(nums.begin(),nums.end(),0)-x;
        if(s<0) return -1;
        vector<int> dp(n,-1);
        int t=0, mx=-1;
        for(int i=0,j=0;i<n;i++){
            t+=nums[i];
            while(j<=i && t>s) t-=nums[j++];
            if(t==s) mx=max(mx,i-j+1);
            dp[i]=mx;
        }
        return mx==-1 ? -1:n-mx;
        
    }
};