class Solution {
public:
    int arithmeticTriplets(vector<int>& a, int d) {
        bitset<201> b;
        int ans=0;
        for(int x:a){
            if(x>=2*d) ans+=b[x-d]&&b[x-2*d];
            b[x]=1;
        }
        return ans;
    }
};