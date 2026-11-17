class Solution {
public:
    int minimumChanges(string s, int k) {
        int n = s.size();
        vector<vector<int>> g(n + 1, vector<int>(n + 1, 1e9));
        vector<vector<int>> dp(n + 1, vector<int>(k + 1, 1e9));
        dp[0][0] = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = i; j <= n; j++) {
                int m = j - i + 1;
                for (int d = 1; d < m; d++) {
                    if (m % d) continue;
                    int cnt = 0;
                    for (int l = 0; l < m; l++) {
                        int r = (m / d - 1 - l / d) * d + l % d;
                        if (l >= r) break;
                        cnt += s[i - 1 + l] != s[i - 1 + r];
                    }
                    g[i][j] = min(g[i][j], cnt);
                }
            }
        }
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= k; j++) {
                for (int h = 0; h < i - 1; h++) {
                    dp[i][j] = min(dp[i][j], dp[h][j - 1] + g[h + 1][i]);
                }
            }
        }
        return dp[n][k];
    }
};