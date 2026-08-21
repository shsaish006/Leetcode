class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        from math import gcd 
        n=len(coins)
        l,r=1,10**11 
        def f(x):
            c=0 
            for m in range(1,1<<n):
                v=1
                s=-1
                for j in range(n):
                    if m&(1<<j):
                        v=v*coins[j]//gcd(v,coins[j])
                        s=-s 
                        if v>x:
                            break 
                if v<=x:
                    c+=s*(x//v)
            return c>=k 
        while l<r:
            m=(l+r)//2 
            if f(m):
                r=m 
            else:
                l=m+1 
        return l
        