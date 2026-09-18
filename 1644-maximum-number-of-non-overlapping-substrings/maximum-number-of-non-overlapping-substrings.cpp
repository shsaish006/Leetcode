class Solution {
public:
    vector<string> maxNumOfSubstrings(string s) {
        int n=s.size();
        vector<int> a(26,n), b(26,-1);
        for(int i=0;i<n;i++){
            int x= s[i]-'a';
            a[x]=min(a[x],i);
            b[x]=i;
        }
        vector<pair<int,int>> v;
        for(int i=0;i<26;i++){
            if(b[i]==-1) continue;
            int l= a[i], r=b[i];
            bool ok=1;
            // int m=0;
            for(int j=l;j<=r;j++){
            int x=s[j]-'a';
            if(a[x]<l){
                ok=0;
                break;
            }
            r=max(r,b[x]);
        }
        //     m|= 1<<(s[j]-'a');
        //     bool ok=1;
        //     for(int j=0;j<26;j++){
        //          if((m>>j &1)&& a[j]<l){
        //         ok=0;
        //         break;
        //     }
        //     if(m>>j &1) r=max(r,b[j]);
        // }
        if(ok) v.push_back({r,l});
        }
        sort(v.begin(),v.end());
        vector<string> ans;
        int dp=-1;
        for(auto [r,l]:v){
            if(l>dp){
                ans.push_back(s.substr(l,r-l+1));
                dp=r;
            }
        }
        return ans;
        
    }
};