class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict 
        g=defaultdict(list)
        d=defaultdict(int)
        for a, b in pairs:
            g[a].append(b)
            d[a]+=1 
            d[b]-=1 
        x=next((x for x  in d if d[x]==1),pairs[0][0])
        a=[]
        def f(x):
            while g[x]:
                f(g[x].pop())
            a.append(x)
        f(x)
        a.reverse()
        return list (zip(a,a[1:]))
        