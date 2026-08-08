class Solution {
public:
    vector<int> validSequence(string a, string b) {
        int n=a.size(), m=b.size(), r=m-1, c=0, j=0;
        vector<int> v(n), ans;
        for(int i=n-1;i>=0;i--){
            v[i]=c;
            if(r>=0&& a[i]==b[r])r--, c++;
        }
        bool x=0;
        for(int i=0;i<n&& j<m ;i++){
            if(a[i]==b[j]){
                ans.push_back(i);
                j++;
            }
            else if (!x&& v[i]>=m-1-j){
                ans.push_back(i);
                j++;
                x=1;
            }
        }
        if(j==m) return ans;
        return {};
        
    }
};