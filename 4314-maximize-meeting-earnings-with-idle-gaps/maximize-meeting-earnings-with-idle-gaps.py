class Solution:
    def maxEarnings(self, met: list[list[int]]) -> int:
        met.sort()
        a=sorted(set(x[1] for x in met))
        n=len(a)
        t=[float('-inf')]*(n+1)
        ans=0 
        def upd(i,x):
            while i<=n:
                t[i]=max(t[i],x)
                i+=i&-i 
        def qry(i):
            x=float('-inf')
            while i:
                x=max(x,t[i])
                i-=i&-i
            return x
        for s,e,v in met:
            x=qry(bisect_right(a,s))
            x=v+max(0,s+x)
            upd(bisect_left(a,e)+1,x-e)
            ans=max(ans,x) 
        return ans
        