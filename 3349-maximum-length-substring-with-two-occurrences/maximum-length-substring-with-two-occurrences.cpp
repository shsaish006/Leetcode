class Solution {
public:
    int maximumLengthSubstring(string s) {
        int a[26]{}, b = 0, c = 0;
        for (int d = 0; d < s.size(); d++) {
            a[s[d] - 'a']++;
            while (a[s[d] - 'a'] > 2) a[s[b++] - 'a']--;
            c = max(c, d - b + 1);
        }
        return c;
    }
};