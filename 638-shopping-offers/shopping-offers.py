class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n=len(needs)
        s=[]
        for x in special:
            if x[n]>=sum(x[i]*price[i] for i in range(n)):
                continue 
            if all (x[i]<=needs[i] for i in range(n)):
                s.append(x)
        dp={tuple(needs):0}
        q=[tuple(needs)]
        k=0 
        while k<len(q):
            a=q[k]
            k+=1 
            for x in s:
                b=[]
                ok=1 
                for i in range(n):
                    if a[i]<x[i]:
                        ok=0 
                        break 
                    b.append(a[i]-x[i])
            
        # for a in q:
        #     c=dp[a] + sum(a[i]*price[i] for i in range(n))
        #     for x in s:
        #         b=[]
        #         ok=1 
        #         for i in range(n):
        #             if a[i]<x[i]:
        #                 ok=0 
        #                 break 
        #             b.append(a[i]-x[i])
                if ok:
                    b=tuple(b)
                    v=dp[a]+x[n]
                    if   v<dp.get(b,10**9):
                        if b not in dp:
                            q.append(b)
                        dp[b]=v
                    # v=dp.get(b,10**9)
                    # if c>v:
                    #     c=v 
            # dp[a]=min(dp[a],c)
            # for x in s:
            #     b=[]
            #     ok=1 
            #     for i in range(n):
            #         if a[i]<x[i]:
            #             ok=0 
            #             break 
            #         b.append(a[i]-x[i])
            #     if ok:
            #         b=tuple(b)
            #         if b not in dp:
            #             dp[b]=dp[a]+x[n]
            #             q.append(b)
        ans=10**9 
        for a,v in dp.items():
            c=v 
            for i in range(n):
                c+=a[i]*price[i]
            ans=min(ans,c)
        return ans
        # for a in dp:
        #     c=dp[a]
        #     for i in range(n):
        #         c+=a[i]*price[i]
        #     ans=min(ans,c)
        # return ans
        #             else:
        #                 dp[b]=min(dp[b],dp[a]+x[n])
        # return dp[(0,)*n]

        # b=[x+1 for x in needs]
        # m=1 
        # for x in b:
        #     m*=x
        # # m=11**n 
        # dp=[10**9]*m 
        # for x in range(m):
        #     y=x 
        #     c=0 
        #     z=1 
        #     a=[0]*n 

        #     for i in range(n):
        #         a[i]=y%b[i] 
        #         y//=b[i]
        #         c+=a[i]*price[i]
        #     dp[x]=c 
        #     for s in special:
        #         ok=1 
        #         t=0 
        #         z=1 
        #         for i in range(n):
        #             if a[i]<s[i]:
        #                 ok=0 
        #                 break 
        #             t+=(a[i]-s[i])*z 
        #             z*=b[i]
        #             # z*=11
        #         if ok:
        #             dp[x]=min(dp[x],s[n]+dp[t])

        # x=0 
        # z=1 
        # for i in range(n):
        #     x+=needs[i]*z 
        #     z*=b[i]
        #     # z*=11 
        # return dp[x]
        