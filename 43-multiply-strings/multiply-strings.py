class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=="0" or num2=="0":
            return "0"
        n,m=len(num1),len(num2)
        a=[0]*(n+m)
        d=len("0123456789")
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                x=int(num1[i])*int(num2[j])
                k=i+j+1 
                a[k]+=x 
                a[k-1]+=a[k]//d
                a[k]%=d 
        i=0 
        while i<len(a) and a[i]==0:
            i+=1 
        return "".join(map(str,a[i:]))