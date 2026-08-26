class Solution {
public:
    string shortestBeautifulSubstring(string s, int k) {
        string a;
        int l=0, c=0;
        for(int r=0;r<s.size();r++){
            c+=s[r]=='1';
            while (c>k) c-=s[l++]=='1';
            while (c==k && s[l]=='0') l++;
            if(c==k){
                string t;
                for(int i=l;i<=r;i++) t+=s[i];
                if(a.empty()) a=t;
                else if (t.size()<a.size()) a=t;
                else if (t.size()==a.size()){
                    if(t<a) a=t;
                }
            }
        }
        return a;
        
    }
};