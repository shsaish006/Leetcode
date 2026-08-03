class Solution {
public:
    vector<int> answerQueries(vector<int>& nums, vector<int>& queries) {
        sort(nums.begin(), nums.end());
        for(int i=1;i<nums.size();i++) nums[i]+=nums[i-1];
        vector<int> ans;
        for(int x:queries){
            int l=0, r=nums.size();
            while(l<r){
                int m=(l+r)/2;
                if(nums[m]<=x) l=m+1;
                else r=m;
            }
            ans.push_back(l);
        }
        return ans;
        
    }
};