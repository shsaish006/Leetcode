class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        n=len(caption)
        if n<3:
            return ""
        inf=10**18
        dp=[inf]*(n+1)
        nxt=[-1]*(n+1)
        ch=[-1]*(n+1)
        sai=[""]*(n+1)

        # dp=[10**18]*(n+1)
        # ans=[""]*(n+1)
        dp[n]=0 
        for i in range(n-3,-1,-1):

            f=[0]*26 
            for j in range(i,min(n,i+5)):
                # s=caption[i:j]
                # cnt=Counter(s)
                f[ord(caption[j])-97]+=1 
                # f[x]+=1 
                ln=j-i+1 
                if ln<3:
                    continue 
                v=inf 
                # ch=""
                c=0 
                # for x in cnt:
                #     c=sum(abs(ord(x)-ord(y)) for y in s)
                #     if c<v or c==v and x<ch:
                #         v=c 
                #         ch=x
                for k in range(26):
                    if f[k]==0:
                        continue
                    cost=0 
                    for p in range(26):
                        cost+=f[p]*abs(k-p)
                    if cost<v:
                        v=cost 
                        c=k
                    # if f[k]:
                    #     cur=0 
                       
                t=v+dp[j+1]
                cur=(chr(c+97)*ln+sai[j+1])[:6]
                if t<dp[i] or t==dp[i] and cur<sai[i]:
                    dp[i]=t 
                    nxt[i]=j+1 
                    ch[i]=c
                    sai[i]=cur
                # elif t==dp[i]:
                #     if c<ch[i]:
                #         nxt[i]=j+1 
                #         ch[i]=c
                # cur=ch*(j-i)+ans[j]
                # # cur=chr(ch+97)*ln+res[j+1]
                # if t<dp[i] or t==dp[i] and cur<ans[i]:
                #     dp[i]=t 
                #     ans[i]=cur
        ans=[]
        i=0 
        while i<n:
            ans.append(chr(ch[i]+97)*(nxt[i]-i))
            i=nxt[i]
        # return ans[0]
        return ''.join(ans)