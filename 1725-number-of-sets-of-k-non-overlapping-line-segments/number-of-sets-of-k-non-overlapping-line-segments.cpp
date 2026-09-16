class Solution {
public:
    int numberOfSets(int n, int k) {
        const int mod=1e9+7;
        // long long a=1;
        vector<int> a(k+1),b(k+1);
        a[0]=1;
        for(int i=2;i<=n;i++){
            vector<int> c(k+1),d(k+1);
            for(int j=0;j<=k;j++){
                c[j]=((long long)a[j]+b[j])%mod;
                // c[j]=(a[j]+b[j])%mod;
                d[j]=b[j];
                if(j)
                    d[j]=((long long)d[j]+a[j-1]+b[j-1])%mod;
                    // d[j]=(d[j]+a[j-1]+b[j-1])%mod;
                }
            // }
            a=c;
            b=d;
        }
        // for(int i=1;i<n;i++){
        //     for(int j=k;j>=0;j--){
        //         b[j]=(b[j]+a[j])%mod;
        //         if (j) b[j]=(b[j]+b[j-1])%mod;
        //         a[j]=(a[j]+b[j])%mod;
        //     }
        // }

        return ((long long)a[k]+b[k])%mod;
        // return a[k];
        // for(int i=1;i<=2*k;i++) a=a*(n+i-2)%mod;
        // for(int i=1;i<=2*k;i++) a=a*500000004%mod;
        // for(int i=1;i<=k;i++) a=a*500000004%mod;
        // return a;
    }
};