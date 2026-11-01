class Solution {
public:
    int minMoves(vector<int>& nums) {
        long long tot=accumulate(nums.begin(), nums.end(), 0LL);
        int val=*min_element(nums.begin(),nums.end());
        return tot-1LL* val*nums.size();
        
    }
};