// class Solution {
// public:
//     long long countNonDecreasingSubarrays(vector<int>& nums, int k) {
//         int n = nums.size();
//         vector<long long> dp(n + 1);
//         vector<int> nxt(n);
//         stack<int> st;
//         for (int i = n - 1; i >= 0; i--) {
//             while (!st.empty() && nums[st.top()] <= nums[i])
//                 st.pop();
//             nxt[i] = st.empty() ? n : st.top();
//             st.push(i);
//         }
//         vector<long long> pref(n + 1);
//         for (int i = 0; i < n; i++)
//             pref[i + 1] = pref[i] + nums[i];
//         long long ans = 0;
//         for (int i = n - 1; i >= 0; i--) {
//             int l = i, r = n - 1, idx = i;
//             while (l <= r) {
//                 int mid = (l + r) / 2;
//                 long long cost = 0;
//                 int j = i;
//                 while (j <= mid) {
//                     int end = min(mid + 1, nxt[j]);
//                     cost += 1LL * nums[j] * (end - j) - (pref[end] - pref[j]);
//                     j = end;
//                 }
//                 if (cost <= k) {
//                     idx = mid;
//                     l = mid + 1;
//                 } else {
//                     r = mid - 1;
//                 }
//             }
//             dp[i] = idx - i + 1;
//             ans += dp[i];
//         }
//         assert(ans >= 0);
//         return ans;
//     }
// };
class Solution {
public:
    long long countNonDecreasingSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> st(n);
        int head = n, tail = n, r = n - 1;
        long long ans = 0, cnt = 0;
        for (int i = n - 1; i >= 0; i--) {
            while (head < tail && nums[st[head]] <= nums[i]) {
                int idx = st[head++];
                int nxt = head < tail ? st[head] : r + 1;
                cnt += 1LL * (nums[i] - nums[idx]) * (nxt - idx);
            }
            st[--head] = i;
            while (cnt > k) {
                cnt -= nums[st[tail - 1]] - nums[r];
                if (st[tail - 1] == r) tail--;
                r--;
            }
            ans += r - i + 1;
        }
        assert(ans >= 0);
        return ans;
    }
};