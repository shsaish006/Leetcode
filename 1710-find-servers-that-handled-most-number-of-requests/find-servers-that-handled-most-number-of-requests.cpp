// class Solution {
// public:
//     vector<int> busiestServers(int k, vector<int>& arrival, vector<int>& load) {
//         int n = arrival.size();
//         vector<int> dp(k, 0), busy(k, 0);
//         memset(dp.data(), 0, k * sizeof(int));
//         memset(busy.data(), 0, k * sizeof(int));
//         for (int i = 0; i < n; i++) {
//             for (int j = 0; j < k; j++) {
//                 if (busy[j] <= arrival[i]) busy[j] = 0;
//             }
//             int idx = i % k;
//             int curr = -1;
//             for (int j = 0; j < k; j++) {
//                 int val = (idx + j) % k;
//                 if (!busy[val]) {
//                     curr = val;
//                     break;
//                 }
//             }
//             if (curr == -1) continue;
//             dp[curr]++;
//             busy[curr] = arrival[i] + load[i];
//         }
//         int val = 0;
//         for (int i = 0; i < k; i++) {
//             if (dp[i] > val) val = dp[i];
//         }
//         vector<int> ans;
//         for (int i = 0; i < k; i++) {
//             if (dp[i] == val) ans.push_back(i);
//         }
//         return ans;
//     }
// };
class Solution {
    const int INF = INT_MAX;
    vector<pair<int, int>> tm;
    vector<int> seg, dp;
    int n;

    void build(int node, int l, int r) {
        if (l == r) {
            tm[node] = {INF, l};
            seg[node] = l;
            return;
        }
        int mid = (l + r) / 2;
        build(node * 2, l, mid);
        build(node * 2 + 1, mid + 1, r);
        tm[node] = min(tm[node * 2], tm[node * 2 + 1]);
        seg[node] = min(seg[node * 2], seg[node * 2 + 1]);
    }

    void upd(int idx, int val, int node, int l, int r) {
        if (l == r) {
            tm[node] = {val, idx};
            seg[node] = (val == INF ? idx : n);
            return;
        }
        int mid = (l + r) / 2;
        if (idx <= mid) upd(idx, val, node * 2, l, mid);
        else upd(idx, val, node * 2 + 1, mid + 1, r);
        tm[node] = min(tm[node * 2], tm[node * 2 + 1]);
        seg[node] = min(seg[node * 2], seg[node * 2 + 1]);
    }

    int query(int ql, int qr, int node, int l, int r) {
        if (r < ql || l > qr || seg[node] == n) return n;
        if (l == r) return l;
        int mid = (l + r) / 2;
        int idx = query(ql, qr, node * 2, l, mid);
        if (idx != n) return idx;
        return query(ql, qr, node * 2 + 1, mid + 1, r);
    }

public:
    vector<int> busiestServers(int k, vector<int>& arrival, vector<int>& load) {
        n = k;
        tm.assign(4 * k, {INF, -1});
        seg.assign(4 * k, k);
        dp.assign(k, 0);
        build(1, 0, k - 1);

        for (int i = 0; i < arrival.size(); i++) {
            while (tm[1].first <= arrival[i]) {
                int idx = tm[1].second;
                upd(idx, INF, 1, 0, k - 1);
            }

            int idx = query(i % k, k - 1, 1, 0, k - 1);
            if (idx == k) idx = query(0, i % k - 1, 1, 0, k - 1);
            if (idx == k) continue;

            dp[idx]++;
            upd(idx, arrival[i] + load[i], 1, 0, k - 1);
        }

        int val = 0;
        for (int i = 0; i < k; i++) {
            if (dp[i] > val) val = dp[i];
        }

        vector<int> ans;
        for (int i = 0; i < k; i++) {
            if (dp[i] == val) ans.push_back(i);
        }
        return ans;
    }
};