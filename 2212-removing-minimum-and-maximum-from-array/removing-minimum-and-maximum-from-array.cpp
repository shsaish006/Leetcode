class Solution {
public:
    int minimumDeletions(vector<int>& a) {
        int n = a.size(), x = 0, y = 0;
        for (int i = 1; i < n; i++) {
            if (a[i] < a[x]) x = i;
            if (a[i] > a[y]) y = i;
        }
        if (x > y) swap(x, y);
        return min({y + 1, n - x, x + 1 + n - y});
    }
};