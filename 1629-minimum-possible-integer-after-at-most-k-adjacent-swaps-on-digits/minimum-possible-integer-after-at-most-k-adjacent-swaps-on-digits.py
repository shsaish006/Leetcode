class Solution:
    def minInteger(self, num: str, k: int) -> str:
        from collections import defaultdict, deque 
        n=len(num)
        p=defaultdict(deque)
        for i,x in enumerate(num,1):
            p[x].append(i)
        t=[0]*(n+1)
        def f(x):
            return x&-x 
        def add(x):
            while x<=n:
                t[x]+=1 
                x+=f(x)
        def get(x):
            s=0 
            while x:
                s+=t[x]
                x-=f(x)
            return s 
        ans=[]
        for i in range(1,n+1):
            for x in '0123456789':
                if p[x]:
                    j=p[x][0]
                    d=j-i+get(n)-get(j)
                    if d<=k:
                        k-=d
                        p[x].popleft()
                        ans.append(x)
                        add(j)
                        break 
        return ''.join(ans)