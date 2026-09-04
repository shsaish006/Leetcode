class Solution {
public:
    int firstStableIndex(vector<int>& a, int k) {
        int n = a.size(), mx = 0, mn = a[n - 1];
        for (int i = n - 1; i >= 0; i--)
            mn = min(mn, a[i]);
            for (int i = 0; i < n; i++) {
            mx = max(mx, a[i]);
            if (mx - *min_element(a.begin() + i, a.end()) <= k)
                return i;
        }
        return -1;
    }
};