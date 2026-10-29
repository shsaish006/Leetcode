class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        sai=[n,edges,s,queries]
        n,nums,s,vals=sai 
        class A:
            def __init__ (self,a):
                self.a=[0]*(a+1)
                self.b=a 
            def add(self, i,val):
                i+=1 
                while i<=self.b :
                    self.a[i]^=val 
                    i+=i&-i
            def pref(self,i):
                i+=1 
                curr=0 
                while i>0:
                    curr^=self.a[i]
                    i-=i&-i 
                return curr 
        a=[[] for i in range(n)]
        for i in nums:
            a[i[0]].append(i[1])
            a[i[1]].append(i[0])
        b=[-1]*n 
        c=[0]*n 
        d=[0]*n 
        # temp=[0]
        # while temp:
        #     curr=temp.pop()
        #     for val in a[curr]:
        #         if val==b[curr]:
        #             continue 
        #         b[val]=curr 
        #         c[val]=c[curr]+1 
        #         temp.append(val)
        # idx=1 
        # while idx<=n:
        #     idx<<=1
        # nums2=[[-1]*n for i in range(20)]
        # for i in range(n):
        #     nums2[0][i]=b[i]
        # for i in range(1,20):
        #     for j in range(n):
        #         if nums2[i-1][j]!=-1:
        #             nums2[i][j]=nums2[i-1][nums2[i-1][j]]
        # def lll(i,j):
        #     if c[i]<c[j]:
        #         i,j=j,i
        o=[-1]*n 
        idx=[]
        temp=[0]
        while temp:
            curr=temp.pop()
            idx.append(curr)
            for val in a[curr]:
                if val==b[curr]:
                    continue 
                b[val]=curr 
                c[val]=c[curr]+1 
                temp.append(val)
        for i in range(n-1,-1,-1):
            curr=idx[i]
            d[curr]=1 
            for val in a[curr]:
                if val==b[curr]:
                    continue 
                d[curr]+=d[val]
                if o[curr]==-1 or d[val]>d[o[curr]]:
                    o[curr]=val 
        nums2=[0]*n 
        vals2=[0]*n 
        idx=0 
        temp=[(0,0)]
        while temp:
            curr,val=temp.pop()
            while curr!=-1:
                nums2[curr]=val 
                vals2[curr]=idx 
                idx+=1 
                for nxt in a[curr]:
                    if nxt!=b[curr] and nxt!=o[curr]:
                        temp.append((nxt,nxt))
                curr=o[curr]
        # def add(i,val):
        #     i+=1 
        #     while i<=n:
        #         nums[i]^=val
        #         i+= i&-i
        # def query(i):
        #     i+=1 
        #     curr=0 
        #     while i>0:
        #         curr^=nums[i]
        #         i-=i&-i 
        #     return curr
        # s=list(s)
        # for i in range(n):
        #     val=1<<(ord(s[i])-97)
        #     add(vals2[i],val)
        # def get(i,j):
        #     curr=0 
        #     while nums2[i]!=nums2[j]:
        #         if c[nums2[i]]<c[nums2[j]]:
        #             i,j=j,i 
        #         curr^=query(vals2[i])^query(vals2[nums2[i]])
        #         i=b[nums2[i]]
        #     if c[i]>c[j]:
        #         i,j=j,i 
        #     curr^=query(vals2[j])^query(vals2[i]-1)
        #     return curr
        ffs=A(idx)
        for i in range(n):
            ffs.add(vals2[i],1<<(ord(s[i])-97))
        def query(i,j):
            curr=0 
            while nums2[i]!=nums2[j]:
                if c[nums2[i]]<c[nums2[j]]:
                    i,j=j,i 
                curr^=ffs.pref(vals2[i])^ffs.pref(vals2[nums2[i]]-1)
                i=b[nums2[i]]
            if c[i]>c[j]:
                i,j=j,i 
            curr^=ffs.pref(vals2[j])^ffs.pref(vals2[i]-1)
            return curr 
        ans=[]
        for i in vals:
            parts=i.split()
            if parts[0]=="update":
                j=int(parts[1])
                k=parts[2]
                val=vals2[j]
                curr=1<<(ord(s[j])-97)
                nxt=1<<(ord(k)-97)
                if curr^nxt:
                    ffs.add(val,curr^nxt)
                s=s[:j]+k+s[j+1:]
            else:
                j=int(parts[1])
                k=int(parts[2])
                curr=query(j,k)
                ans.append(curr &(curr-1)==0)
            # if i[0]=='u':
            #     j=int(i.split(',')[0][2:])
            #     k=i[-1]
            #     val=vals2[j]
            #     curr=1<<(ord(s[j])-97)
            #     nxt=1<<(ord(k)-97)
            #     if curr^nxt:
            #         ffs.add(val,curr^nxt)
            #     s=s[:j]+k+s[j+1:]
            # else:
            #     j=int(i.split(',')[0][2:])
            #     k=int(i.split(',')[1])
            #     curr=query(j,k)
            #     ans.append(curr&(curr-1)==0)
        return ans

        