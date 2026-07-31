class Solution {
public:
    int minimumPushes(string s) {
        vector<int> a(26);
        for (char c : s)
            a[c - 'a']++;
        sort(a.rbegin(), a.rend());
        int ans = 0;
        for (int i = 0; i < 26; i++)
            ans += (i / 8 + 1) * a[i];

        return ans;
    }
};