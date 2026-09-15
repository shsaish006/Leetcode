class Solution {
public:
    int maxPalindromes(string s, int k) {
        int n=s.length();
        vector<vector<bool>> aaa(n,vector<bool>(n,false));
        for(int i=n-1;i>=0;i--){
            for(int j=i;j<n;j++){
                if(s[i]==s[j]&& ((j-i+1<=2)||(aaa[i+1][j-1]))){
                    aaa[i][j]=true;
                }
            }
        }
        int l=-1;
        int cnt=0;
        for(int r=0;r<n;r++){
            for(int le =l+1;le<=r-k+1;le++){
            if(aaa[le][r]){
                cnt++;
                l=r;
                break;
            }
        }
        }
        return cnt;
        
    }
};