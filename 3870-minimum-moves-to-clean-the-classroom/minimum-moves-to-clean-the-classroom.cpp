class Solution {
public:
    int minMoves(vector<string>& a, int e) {
        int m = a.size(), n = a[0].size(), x, y, c = 0;
        vector<vector<int>> id(m, vector<int>(n, -1));
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++) {
                if (a[i][j] == 'S') x = i, y = j;
                if (a[i][j] == 'L') id[i][j] = c++;
            }
            if (!c) return 0;
        int M = 1 << c;
        vector<vector<vector<vector<char>>>> v(
            m, vector<vector<vector<char>>>(
                n, vector<vector<char>>(e + 1, vector<char>(M))));
        queue<array<int,4>> q;
        q.push({x, y, e, M - 1});
        v[x][y][e][M - 1] = 1;
        int d[5] = {-1, 0, 1, 0, -1}, ans = 0;
        while (!q.empty()) {
            int z = q.size();
            while (z--) {
                auto [i, j, en, mask] = q.front();
                q.pop();
                if (!mask) return ans;
                if (!en) continue;
                for (int k = 0; k < 4; k++) {
                    int ni = i + d[k], nj = j + d[k + 1];
                    if (ni < 0 || ni >= m || nj < 0 || nj >= n || a[ni][nj] == 'X')
                        continue;
                    int ne = a[ni][nj] == 'R' ? e : en - 1;
                    int nm = mask;
                    if (a[ni][nj] == 'L')
                        nm &= ~(1 << id[ni][nj]);
                    if (!v[ni][nj][ne][nm]) {
                        v[ni][nj][ne][nm] = 1;
                        q.push({ni, nj, ne, nm});
                    }
                }
            }
            ans++;
        }
        return -1;
    }
};