class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        p=list(range(n))
        def f(x):
            while x!= p[x]:
                p[x]=p[p[x]]
                x=p[x]
            return x 
        edgeList.sort(key=lambda x: x[2])
        ans=[0]*len(queries)
        j=0 
        for i,(a,b,l) in sorted(enumerate(queries), key=lambda x: x[1][2]):
            while j<len(edgeList) and edgeList[j][2]<l:
                u,v,_=edgeList[j]
                p[f(u)]=f(v)
                j+=1 
            ans[i]=f(a)==f(b)
        return ans
        