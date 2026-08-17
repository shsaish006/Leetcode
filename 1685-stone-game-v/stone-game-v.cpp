class Solution {
public:
    int stoneGameV(vector<int>& a) {
        int n=a.size();
        vector<int> s(n+1), dp(n,0);
        for(int i=0;i<n;i++)
        s[i+1]=s[i]+a[i];
        vector<vector<int>> d(n, vector<int>(n));
        for(int l=2;l<=n;l++)
        for(int ll=0;ll+l<=n;ll++){
            int r= ll+l-1;
            for(int m=ll;m<r;m++){
                int x= s[m+1]-s[ll];
                int y= s[r+1]-s[m+1];
                if(x<=y)
                d[ll][r]=max(d[ll][r], x+d[ll][m]);
                if(x>=y) d[ll][r]=max(d[ll][r], y+d[m+1][r]);
            }
        }
        return d[0][n-1];
        
    }
};