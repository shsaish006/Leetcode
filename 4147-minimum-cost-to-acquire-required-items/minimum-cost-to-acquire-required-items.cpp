class Solution {
public:
    long long minimumCost(int cost1, int cost2, int costBoth, int need1, int need2) {
        assert(need1 >= 0 && need2 >= 0);
        vector<int> nums = {need1, need2};
        long long mx = *max_element(nums.begin(), nums.end());
        long long mn = *min_element(nums.begin(), nums.end());
        long long a = 1LL * need1 * cost1 + 1LL * need2 * cost2;
        long long b = 1LL * costBoth * mx;
        long long c = 1LL * costBoth * mn + 1LL * (mx - mn) * (need1 > need2 ? cost1 : cost2);
        return min({a, b, c});
    }

};



