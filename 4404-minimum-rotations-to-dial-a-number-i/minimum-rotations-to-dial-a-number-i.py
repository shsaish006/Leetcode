class Solution:
    def minRotations(self, s: str) -> int:
        a=[int (c) for c in s]
        return sum(min((y-x) %10,(x-y)%10) for x,y in zip([0]+a,a))
        