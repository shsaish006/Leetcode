class Solution {
public:
    int longestSubsequence(vector<int>& a) {
        int x=0, z=0;
        for(int v:a) x^=v, z+=!v;
        return x? a.size():z==a.size()?0:a.size()-1;
        
    }
};