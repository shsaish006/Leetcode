class Solution {
public:
    //  q= queryCharacters idx= queryIndices
    vector<int> longestRepeating(string s, string q, vector<int>& idx) {
        int n=s.size();
        set<int> a;
        multiset<int> b;
        for(int i=1;i<n;i++)
        if(s[i]!=s[i-1])
        a.insert(i);
        int p=0;
        for(int x:a){
            b.insert(x-p);
            p=x;
        }
        b.insert(n-p);
        vector<int> ans;
        for(int k=0;k<idx.size();k++){
            int x=idx[k];
            char v= q[k];
            if(s[x]==v){
                ans.push_back(*b.rbegin());
                continue;
            }
            if(x>0 && s[x]!=s[x-1]){
                int l=*prev(a.lower_bound(x));
                int r= a.lower_bound(x)== a.end() ? n: *a.lower_bound(x);
            }
            auto add= [&](int x){
                if(x>0&& x<n && s[x]!=s[x-1])
                a.insert(x);
            };
            auto rem= [&](int x){
                if(x>0 && x<n)
                a.erase(x);
            };
            auto calc= [&](int x){
                int l=0, r=n;
                auto it =a.lower_bound(x);
                if(it!= a.begin()) l= *prev(it);
                if(it!=a.begin()) r= *it;
                return pair<int,int>(l,r);
            };
            for(int z: {x,x+1}){
                if(z>0 && z< n && a.count(z)){
                    auto it=a.find(z);
                    int l= it==a.begin()?0 : *prev(it);
                    int r= next(it)==a.end()? n: *next(it);
                    b.erase(b.find(z-l)); 
                    b.erase(b.find(r-z)); 
                    b.insert(r-l); 
                    a.erase(it); 
                }
            }
            s[x]=v;
            for(int z:{x,x+1}){
                if(z>0 && z<n && s[z]!= s[z-1]){
                    auto it =a.lower_bound(z);
                    int l= it==a.begin()? 0: *prev(it);
                    int r=it==a.end()? n: *it;
                    b.erase(b.find(r-l));
                    b.insert(z-l);
                    b.insert(r-z);
                    a.insert(z);
                }
            }
            ans.push_back(*b.rbegin());


        }
        return ans;
        
    }
};