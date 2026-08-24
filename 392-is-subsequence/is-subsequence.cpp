class Solution {
public:
    bool isSubsequence(string s, string t) {
        vector<bitset<100001>> b(26);
        for(int i=0;i<t.size();i++) b[t[i]-'a'][i]=1;
        int p=0;
        for(char c:s){
            bitset<100001> x=b[c-'a']>>p;
            if(!x.any()) return 0;
            p=x._Find_first()+p+1;
            // if(!b[c]) return 0;
        }
        return 1;
        
    }
};