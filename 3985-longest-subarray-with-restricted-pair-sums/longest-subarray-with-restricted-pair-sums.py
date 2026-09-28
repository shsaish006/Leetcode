class Solution:
    def maxSubarray(self, nums: List[int]) -> int:
        c,a,p,={},[],{}
        l=ans=0 
        for r,x in enumerate(nums):
            for v in a:
                p[x+v]=p.get(x+v,0)+c[v]
            if x not in c:
                insort(a,x)
                c[x]=0 
            c[x]+=1 
            while any(p.get(v,0) for v in a):
                y=nums[l]
                c[y]-=1 
                for v in a:
                    if c[v]:
                        p[y+v]-=c[v]
                if not c[y]:
                    a.pop(bisect_left(a,y))
                    del c[y]
                l+=1 
            ans=max(ans,r-l+1)
        return ans