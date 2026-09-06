class Solution {
public:
    int numDistinct(string s, string t) {
        int n = t.size();
        vector<unsigned long long> a(n + 1);
        a[0] = 1;
        for (char c : s)
            for (int j = n; j; --j)
                if (c == t[j - 1])
                    a[j] += a[j - 1];

        return a[n];
    }
};