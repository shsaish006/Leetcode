class Solution {
public:
    int numOfSubarrays(vector<int>& arr) {
        int cnt[2]={1,0}, ans=0, tot=0;
        for(int val:arr){
            tot=(tot+val)%2;
            ans=(ans+cnt[tot^1])%1000000007;
            cnt[tot]++;
        }
        return ans;
    }
};