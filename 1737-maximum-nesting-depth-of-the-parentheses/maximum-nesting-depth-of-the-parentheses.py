class Solution:
    def maxDepth(self, s: str) -> int:
        d=ans=0 
        for c in s:
            d+=(c=='(')-(c==')')
            if d>ans:
                ans=d 
        return ans
        