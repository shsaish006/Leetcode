class Solution:
    def minCostToEqualizeArray(self, nums: List[int], cost1: int, cost2: int) -> int:
        mod=10**9+7 
        n=len(nums)
        mx=max(nums)
        s=sum(nums)
        if n==1:
            return 0 
        if n==2:
            return (mx-min(nums))*cost1%mod
        req=mx*n-s
        if 2*cost1<cost2:
            return req*cost1%mod
        h=mx*n-s
        if 2*cost1<=cost2:
            return req*cost1%mod
        h=mx-min(nums)
            # return (mx*2-s)*cost1%mod
        # if cost2>=2*cost1:
        #     return (mx*n-s)*cost1%mod
        if req>=2*h:
            x=req//2 
            h=req-2*x
        else:
            x=req-h 
            h-=x 
        ans=x*cost2
        def f(h):
            res=h*cost1 
            if h+1<n:
                x=(h+n)//2 
                if h+n-2*x:
                    if n&1:
                        res=min(res,x*cost2+min(cost1,(n+1)//2*cost2))
                    else:
                        res=min(res,x*cost2+cost1)
                else:
                    res=min(res,x*cost2)
            else:
                d=n-2 
                x=h//d 
                res=min(res,f(h-x*d)+x*(n-1)*cost2)
            return res
        return (ans+f(h))%mod
            
        # d=mx-min(nums)
        # mn=min(nums)
        # req=mx*n-s
        # d=mx-mn
        # ans=req*cost1
        # for t in [mx,mx+max(0,(req-2*d+n-3)//(n-2)),mx+max(0,(req-2*d+n-3)//(n-2))+1]:
        #     x=n*t-s
        #     a=t-mn
        #     p=min(x//2,x-a)
        #     cur=p*cost2+(x-2*p)*cost1 

        # for x in [0,1]:
        #     t=mx+(req-d+n-3)//(n-2)+x 
        #     ext=n*t-s
        #     p=min(ext//2,ext-(t-mx)) 
        #     ans=min(ans,cur)
        # return ans %mod


       
        