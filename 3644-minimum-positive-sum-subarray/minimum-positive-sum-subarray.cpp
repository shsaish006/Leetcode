class Solution {
public:
    int minimumSumSubarray(vector<int>& nums, int l, int r) {
        int n=nums.size();
        vector<int> vals(n+1,0);
        for(int i=0;i<n;i++) vals[i+1]=vals[i]+nums[i];
        multiset<int> ok;
        int ans=1e9;
        for(int i=l;i<=n;i++){
            ok.insert(vals[i-l]);
            if(i>r) ok.erase(ok.find(vals[i-r-1]));
            auto it=ok.upper_bound(vals[i]-1);
            if(it!=ok.begin()){
                ans=min(ans,vals[i]-*prev(it));
            }
        }
        return ans==1e9?-1:ans;
        
    }
};