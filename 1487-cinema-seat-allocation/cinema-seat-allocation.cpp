class Solution {
public:
    int maxNumberOfFamilies(int n, vector<vector<int>>& a) {
        sort(a.begin(),a.end());
        int m[3]={480,30,120};
        int ans=2*n, i=0;
        while(i<a.size()){
            int row=a[i][0], x=0;
            while(i<a.size()&& a[i][0]==row){
                x|= 1<<(10-a[i][1]);
                i++;
            }
        
        // vector<int> d(n+1);
        // vector<int> v(n+1);
        // int cnt=0;
        // for(auto &x:a){
        //     d[x[0]] |= 1<< (10-x[1]);
        //     if(!v[x[0]]){
        //     v[x[0]]=1;
        //     cnt++;
        // }
        // }
        int c=0;
        for(auto y:m){
            if(!(x&y)){
                x|=y;
                c++;
            }
        }
        // int m[3]={480,30,120};
        // // int ans= (n-a.size())*2; 
        // int ans= (n-cnt)*2;
        // for(int i=1;i<=n;i++){
        //     if(!v[i]) continue;
        //     int x=d[i];
        //     int c=0;
        //     for(auto y:m){
        //         if(!(x&y)){
        //             x|=y;
        //             c++;
        //         }
        //     }
        ans-=2;
        ans+=c;
            // ans+=c;
        }
        return ans;
        
    }
};