class Solution {
public:
    string mergeAlternately(string a, string b) {
        string s;
        int n=min(a.size(),b.size());
        for(int i=0;i<n;i++) s+=a[i], s+=b[i];
        s+=a.substr(n);
        s+=b.substr(n);
        return s;
        
    }
};