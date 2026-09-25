class Solution {
public:
    long long minCost(vector<int>& basket1, vector<int>& basket2) {
        unordered_map<int, int> freq;
        int n = basket1.size();
        for (int i = 0; i < n; ++i) {
            freq[basket1[i]]++;
            freq[basket2[i]]--;
        }

        vector<int> toSwap;
        int minValue = INT_MAX;
        for (auto& [num, count] : freq) {
            if (count % 2 != 0) return -1;
            int half = abs(count) / 2;
            for (int i = 0; i < half; ++i) toSwap.push_back(num);
            minValue = min(minValue, num);
        }

        sort(toSwap.begin(), toSwap.end());

        long long totalCost = 0;
        int m = toSwap.size();
        for (int i = 0; i < m / 2; ++i)
            totalCost += min(toSwap[i], 2 * minValue);

        return totalCost;
    }
};
