class Solution {
public:
    string lexGreaterPermutation(string s, string target) {
        int n=s.size();
        vector<int> a(26);
        for(char c:s) a[c-'a']++;
        for(int i=n-1;i>=0;i--){
            vector<int> b=a;
            bool ok=1;
            for(int j=0;j<i;j++){
                int x=target[j]-'a';
                if(!b[x]){
                    ok=0;
                    break ;
                }
                b[x]--;
            }
            if(!ok) continue;
            for(int x=target[i]-'a'+1; x<26;x++){
                if(!b[x]) continue;
                string ans= target.substr(0,i);
                ans+=char('a'+x);
                b[x]--;
                for(int j=0;j<26;j++) ans.append(b[j], char('a'+j));
                return ans;
            }
        }
        return "";
        
    }
};