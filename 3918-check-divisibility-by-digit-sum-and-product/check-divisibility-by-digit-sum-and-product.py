class Solution:
    def checkDivisibility(self, n: int) -> bool:
        a=list(map(int,str(n)))
        return n%(sum(a)+ __import__('math').prod(a))==0
        