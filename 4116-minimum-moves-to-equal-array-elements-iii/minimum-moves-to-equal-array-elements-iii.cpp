class Solution {
public:
    int minMoves(vector<int>& nums) {
        assert(!nums.empty());
        sort(nums.begin(), nums.end());
        return 1LL*nums.back()*nums.size()-accumulate(nums.begin(), nums.end(),0LL);
        
    }
};