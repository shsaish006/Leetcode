class Solution {
public:
    int minInsertions(string s) {
        string t=s;
        reverse(t.begin(),t.end());
        int n=s.size();
        vector<int> d(n+1);
        for(int i=1;i<=n;i++){
            vector<int> a=d;
            for(int j=1;j<=n;j++)
            if(s[i-1]==t[j-1]) a[j]=d[j-1]+1;
            else a[j]=max(d[j],a[j-1]);
            d=a;
        }
        return n-*max_element(d.begin(),d.end());
        
    }
};