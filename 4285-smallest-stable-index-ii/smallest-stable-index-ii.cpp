class Solution {
public:
    int firstStableIndex(vector<int>& nums, int k) {
        int n = nums.size(), mx = 0;
        vector<int> r = nums;
        for (int i = n - 2; i >= 0; i--)
            r[i] = min(r[i], r[i + 1]);
        for (int i = 0; i < n; i++) {
            mx = max(mx, nums[i]);
            if (mx - r[i] <= k) return i;
        }
        return -1;
    }
};