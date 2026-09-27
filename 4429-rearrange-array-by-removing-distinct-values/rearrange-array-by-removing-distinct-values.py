class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        d={}
        k=[]
        for x in nums:
            if x not in d:
                d[x]=0 
                insort(k,x)
            d[x]+=1 
        a=[]
        while k:
            b=[]
            for x in k:
                a.append(x)
                d[x]-=1 
                if d[x]:
                    b.append(x)
            k=b 
        return a
        