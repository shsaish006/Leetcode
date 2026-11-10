class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        costs=[0]+costs
        # a=[0]+[float('inf')]*
        a=[float('inf')]*(n+1)
        a[0]=0
        # for b in range(1,n+1):
        #     c=[]
        #     for d in (1,,2,3):
        #         if b-d>=0:
        #             c.append(a[b-d]+cost[b]+d*d)
        for b in range(n):
            for c in range(1,4):
                d=b+c
                if d<=n:
        # for b in range(1,n+1):
        #     a[b]=costs[b]+(a[b-1]+1 if b -1>=0 else float(;inf))
                    e=a[b]+costs[d]+c*c
                    # f=costs[e]+min(a+1,b+4,c+9)
                    if e<a[d]:
                        a[d]=e
        return a[n]
        