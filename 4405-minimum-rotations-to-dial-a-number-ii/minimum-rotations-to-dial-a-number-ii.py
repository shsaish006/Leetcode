class Solution:
    def minRotations(self, n: int, s: str) -> int:
        a=[0]+list(map(int,s))
        d=lambda x,y:min(abs(x-y),10-abs(x-y))
        b=[d(a[i],a[i+1]) for i in range(n)]
        return sum(b)-max(b[i]-d(a[i],a[-1]) for i in range(n))
        