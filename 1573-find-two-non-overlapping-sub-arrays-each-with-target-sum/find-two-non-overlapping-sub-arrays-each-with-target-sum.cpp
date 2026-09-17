class Solution {
public:
    int minSumOfLengths(vector<int>& arr, int target) {
        int n = arr.size(), inf = 1 << 30;
        vector<int> p(n + 1), f(n + 1, inf);
        for (int i = 0; i < n; i++)
            p[i + 1] = p[i] + arr[i];
        int ans = inf;
        for (int i = 0; i < n; i++) {
            int x = p[i] + target;
            int j = lower_bound(p.begin() + i + 1, p.end(), x) - p.begin();
            if (j <= n && p[j] == x) {
                f[j] = min(f[j], j - i);
                if (f[i] != inf)
                    ans = min(ans, f[i] + j - i);
            }

            f[i + 1] = min(f[i + 1], f[i]);
        }

        return ans == inf ? -1 : ans;
    }
};