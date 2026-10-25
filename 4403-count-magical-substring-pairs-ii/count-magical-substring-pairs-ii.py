class Solution:
    def countMagicalPairs(self, s: str) -> int:
        n=len(s)
        left,right=[-1]*26 ,[n]*26 
        l,r=[],[None]*n 
        for i,c in enumerate(s):
            left[ord(c)-97]=i 
            l.append(sorted(left,reverse=True))
        for i in range(n-1,-1,-1):
            right[ord(s[i])-97]=i 
            r[i]=sorted(right)
        return sum((ll[k-1]-(ll[k] if k<26 else -1))*((rr[k] if k<26 else n)-rr[k-1]) for j in range(n-1) for ll,rr in[(l[j],r[j+1])] for k in range(1,27))
        