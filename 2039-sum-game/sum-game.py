class Solution:
    def sumGame(self, num: str) -> bool:
        n=len(num);a=b=c=d=0
        for i in range(n//2):
            if num[i]=='?': a+=1
            else: c+=int(num[i])
        for i in range(n//2,n):
            if num[i]=='?': b+=1
            else: d+=int(num[i])
        if (a+b)%2:return True
        return 2*(c-d)!=9*(b-a)