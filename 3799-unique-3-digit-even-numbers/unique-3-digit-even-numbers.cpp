class Solution {
public:
    int totalNumbers(vector<int>& digits) {
        int f[10]={}, ans=0;
        for(int x:digits) f[x]++;
        for(int i=1;i<10;i++){
            for(int j=0;j<10;j++){
                for(int k=0;k<10;k++){
                    if(k%2||!f[i]|| !f[j]||!f[k]) continue;
                    if(i==j&&j==k&&f[i]<3) continue;
                    if(i==j&&f[i]<2) continue;
                    if(i==k&&f[i]<2) continue;
                    if(j==k&&f[j]<2) continue;
                    ans++;
                }
            }
        }
        return ans;
    }
};






