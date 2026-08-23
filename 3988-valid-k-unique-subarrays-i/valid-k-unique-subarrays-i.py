class Solution:
    def validSubarrays(self, nums: list[int], k: int, q: list[list[int]]) -> list[bool]:
        sai=q
        n=len(nums)
        # p=[0]*(n+1)
        # for i,x in enumerate(nums):
        #     p[i+1]=p[i]^(1<<x)
        # qq=[[] for _ in range(n)]
        # # ans=[Fa]
        v=sorted(set(nums))
        mp={x:i for i,x in enumerate(v)}
        # b=int(n**0.5)+1 
        # qq=list(range(len(q)))
        # qq.sort(key=lambda i:(q[i][0]//b, q[i][1] if (q[i][0]//b)%2==0 else -q[i][1]))
        p=[0]*(n+1)
        z=[0]*len(v)
        # qq=sorted([(l,r,i) for i ,(l,r) in enumerate(q)],key=lambda x:(x[0]//b,x[1] if (x[0]//b)%2==0 else -x[1]))
        # c=[0]*(max(nums)+1)
        # c={}
        # ans=[False]*len(q)
        # d=o=0 
        # l=0 
        # r=-1
        for i in range(n):
            x=mp[nums[i]]
            z[x]^=1 
            p[i+1]=p[i]^(1<<x)
        ans=[False]*len(q)
        qq=[[] for _ in range(n)]
        for i in range(len(q)):
            x,y=q[i]
            if p[y+1]^p[x]==0:
                qq[y].append((x,i))
        t=[0]*(n+1)
        rbk={}
        # for i,(l,r) in enumerate(q):
        #     if p[r+1]==p[l]:
        #         qq[r].append((l,i))
        # z=1 
        # while z<n:
        #     z<<=1
        # t=[0]*(2*z)
        # akh={}
        def add(i,v):
            i+=1
            while i<=n:
                t[i]+=v 
                i+=i&-i
            # nonlocal d,o
            # v=c.get(x,0)
            # if v==0:
            #     d+=1 
            # if v&1:
            #     o-=1 
            # else:
            #     o+=1
            # c[x]=v+1
            # if c[x]==0:
            #     d+=1 
            # if c[x]&1:
            #     o-=1 
            # else:
            #     o+=1 
            # c[x]+=1
        def get(i):
            s=0 
            while i>0:
                s+=t[i]
                i-=i&-i 
            return s
            
        # def rem(x):
        #     nonlocal d,o 
        #     v=c[x]
        #     if v&1:
        #         o-=1 
        #     else:
        #         o+=1 
        #     c[x]=v-1 
        #     if c[x]==0:
        #         d-=1
            # if c[x]&1:
            #     o-=1 
            # else:
            #     o+=1 
            # c[x]-=1 
            # if c[x]==0:
            #     d-=1
        for i in range(n):
            x=nums[i]
            if x in rbk:
                add(rbk[x],-1)
            rbk[x]=i 
            add(i,1)
                
        # for i in qq:
        #     x,y=q[i]
        #     while l>x:
        #         l-=1 
        #         add(nums[l])
        #     while r<y:
        #         r+=1 
        #         add(nums[r])
        #     while l<x:
        #         rem(nums[l])
        #         l+=1
        #     while r>y:
        #         rem(nums[r])
        #         r-=1
        #     ans[i]=d==k and o==0 
        # return ans
            for x,j in qq[i]:
                d=get(i+1)-get(x)
                if d==k :
                    ans[j]=True 
        return ans
                
        # def upd(i,v):
        #     i+=z 
        #     t[i]=v 
        #     while i>1:
        #         i>>=1 
        #         t[i]=t[i<<1]+t[i<<1|1]
        # def qry(l,r):
        #     l+=z 
        #     r+=z 
        #     s=0 
        #     while l<=r:
        #         if l&1:
        #             s+=t[l]
        #             l+=1 
        #         if not r &1:
        #             s+=t[r]
        #             r-=1 
        #         l>>=1 
        #         r>>=1
        #     return s
        # l,r=0,-1 
        # d=o=0 
        # for x,y,i in qq:
            # while r<y:
            #     r+=1 
            #     v=nums[r]
            #     d+=c[v]==0 
            #     o+=1 if c[v]%2==0 else -1 
            #     c[v]+=1 
            # while r>y:
            #     v=nums[r]
            #     o+=1 if c[v]%2==0 else -1
            #     c[v]-=1 
            #     # o+=1 if c[v]%2==0 else -1 
            #     d-=c[v]==0
            #     r-=1 
            # while l<x:
            #     v=nums[l]
            #     o+=1  if c[v]%2==0 else -1
            #     c[v]-=1 
            #     # o+=1 if c[v]%2==0 else -1 
            #     d-=c[v]==0 
            #     l+=1 
            # while l>x:
            #     l-=1 
            #     v=nums[l]
            #     d+=c[v]==0 
            #     o+=1 if c[v]%2==0 else -1
            #     c[v]+=1 
            # while r<y:
            #     r+=1 
            #     v=nums[r]
            #     d+=c[v]==0 
            #     o+=1 if c[v]%2==0 else -1 
            #     c[v]+=1 
            # while l<x:
            #     v=nums[l]
            #     o+=1 if c[v]%2==0 else -1 
            #     c[v]-=1 
            #     d-=c[v]==0
            #     l+=1 
            # while r>y:
            #     v=nums[r]
            #     o+=1 if c[v]%2==0 else -1 
            #     c[v]-=1 
            #     d-=c[v]==0 
            #     r-=1
        #         ans[i]=d==k and o==0
        # # for r,x in enumerate(nums):
        # #     if x in akh:
        # #         upd(akh[x],0)
        # #     akh[x]=r 
        # #     upd(r,1)
        # #     for l,i in qq[r]:
        # #         ans[i]=qry(l,r)==k
        #     return ans
        