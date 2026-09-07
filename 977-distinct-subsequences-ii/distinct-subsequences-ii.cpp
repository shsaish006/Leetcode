class Solution {
public:
    int distinctSubseqII(string s) {
        long long m = 1e9 + 7, t = 0, a['z' - 'a' + 1]{};
        for (char c : s) {
            int i = c - 'a';
            long long x = (t + 1) % m;
            t = (2 * t + 1 - a[i] + m) % m;a[i] = x;
        }
        return t;
    }
};