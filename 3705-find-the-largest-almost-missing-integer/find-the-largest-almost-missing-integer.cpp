class Solution {
public:
    int largestInteger(vector<int>& nums, int k) {
        int n=nums.size();
        if(k==1){
            unordered_map<int,int> m;
            for(int x:nums) m[x]++;
            int ans=-1;
            for(auto[x,c]:m)
            if(c==1) ans=max(ans,x);
        return ans;
        }
        if(k==n) return *max_element(nums.begin(),nums.end());
        int ans=-1;
        if(count(nums.begin()+1,nums.end(),nums[0])==0)
        ans=nums[0];
        if(count(nums.begin(),nums.end()-1,nums[n-1])==0)
        ans=max(ans,nums[n-1]);
        return ans;
        //  wtf is desc 
        
    }
};