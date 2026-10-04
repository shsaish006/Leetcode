class Solution:
    def countGoodStrings(self, n: int) -> int:
        # a,b=0,1 
        def fib(n):
            if not n:
                return 0,1 
            a,b=fib(n//2)
            c=a*(2*b-a)%1000000007
            d=(a*a+b*b)%1000000007
            return (d,(c+d)%1000000007) if n & 1 else (c,d)

        # for _ in range(n):
        #     a,b=b,(a+b)%1000000007 
        return 2*fib(n)[0]%1000000007
        