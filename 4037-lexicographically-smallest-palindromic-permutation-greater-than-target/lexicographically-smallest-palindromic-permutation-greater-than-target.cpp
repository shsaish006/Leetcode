class Solution {
public:
    string buildPalindrome(string half,char middle) {
        string res=half;
        if(middle) res+=middle;
        for(int i=half.size()-1;i>=0;i--)
            res+=half[i];
        return res;
    }
    string smallestGreaterOrEqual(vector<int> cnt,string target) {
        int n=target.size();
        int i=0;
        while(i<n&&cnt[target[i]-'a']) {
            cnt[target[i]-'a']--;
            i++;
        }
        if(i==n) return target;
        for(int pos=i;pos>=0;pos--) {
            if(pos<i)
                cnt[target[pos]-'a']++;
            for(int c=target[pos]-'a'+1;c<26;c++) {
                if(!cnt[c]) continue;
            string res=target.substr(0,pos);
                res+=char('a'+c);
                cnt[c]--;
            for(int j=0;j<26;j++)
                    res+=string(cnt[j],char('a'+j));
                return res;
            }
        }
        return "";
    }

    bool nextPermutation(string &s) {
        int n=s.size(),i=n-2;

        while(i>=0&&s[i]>=s[i+1]) i--;

        if(i<0) return false;

        int j=n-1;
        while(s[j]<=s[i]) j--;

        swap(s[i],s[j]);
        reverse(s.begin()+i+1,s.end());

        return true;
    }

    string lexPalindromicPermutation(string s,string target) {
        vector<int> freq(26);

        for(char c:s)
            freq[c-'a']++;

        char middle=0;
        int odd=0;

        for(int i=0;i<26;i++) {
            if(freq[i]&1) {
                odd++;
                middle=char('a'+i);
            }
        }

        if(odd>1) return "";

        vector<int> cnt(26);
        for(int i=0;i<26;i++)
            cnt[i]=freq[i]/2;

        int k=s.size()/2;
        string targetHalf=target.substr(0,k);

        string half=smallestGreaterOrEqual(cnt,targetHalf);

        if(half.empty()&&k>0)
            return "";

        string ans=buildPalindrome(half,middle);

        if(ans>target)
            return ans;

        if(!nextPermutation(half))
            return "";

        return buildPalindrome(half,middle);
    }
};