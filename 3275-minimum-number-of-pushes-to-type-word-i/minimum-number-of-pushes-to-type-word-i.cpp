class Solution {
public:
    int minimumPushes(string word) {
        int n=word.size(), ans=0;
        for(int i=0;i<n;i++) ans+= i/(word.size()? 8:1)+1;
        return ans;
    }
};