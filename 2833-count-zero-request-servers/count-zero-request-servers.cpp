class Solution {
public:
    vector<int> countServers(int n, vector<vector<int>>& logs, int x, vector<int>& queries) {
        sort(logs.begin(), logs.end(),[](const vector<int> &a, const vector<int> &b){
            return a[1]<b[1];
        });
        int m=queries.size();
        vector<pair<int,int>> vals(m);
        for(int i=0;i<m;i++) vals[i]={queries[i],i};
        sort(vals.begin(), vals.end());
        unordered_map<int,int> cnt;
        vector<int> ans(m);
        int j=0, k=0, tot=0;
        for(auto[r,idx]:vals){
            int l=r-x;
            while(k<logs.size()&& logs[k][1]<=r){
                if(cnt[logs[k][0]]++==0) tot++;
                k++;
            }
            while(j<k && logs[j][1]<l){
                if(--cnt[logs[j][0]]==0) tot--;
                j++;
            }
            ans[idx]=n-tot;
        }
        return ans;
        
    }
};