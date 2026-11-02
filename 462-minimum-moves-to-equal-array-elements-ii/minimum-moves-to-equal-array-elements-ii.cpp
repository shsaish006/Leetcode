class Solution {
public:
    int minMoves2(vector<int>& nums) {
        nth_element(nums.begin(), nums.begin()+nums.size()/2, nums.end());
        int val=nums[nums.size()/2], ans=0;
        for(int curr:   nums) ans+=abs(curr-val);
        return ans;
        
    }
};