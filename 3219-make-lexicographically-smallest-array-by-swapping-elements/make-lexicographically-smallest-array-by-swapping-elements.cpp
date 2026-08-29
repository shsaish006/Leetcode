class Solution {
public:
    vector<int> lexicographicallySmallestArray(vector<int>& nums, int limit) {
        int n = nums.size();
        vector<pair<int,int>> a;
        for (int i = 0; i < n; i++) a.push_back({nums[i], i});
        sort(a.begin(), a.end());
        vector<int> ans(n);
        for (int i = 0; i < n;) {
            int j = i + 1;
            while (j < n && a[j].first - a[j - 1].first <= limit) j++;
            vector<int> v;
            for (int k = i; k < j; k++) v.push_back(a[k].second);
            sort(v.begin(), v.end());
            for (int k = i; k < j; k++)
                ans[v[k - i]] = a[k].first;i = j;
        }return ans;
    }
};