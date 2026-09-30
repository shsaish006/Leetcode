class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        x=0 
        ans=[]
        for c in seq:
            if c=='(':
                ans.append(x&1)
                x+=1 
            else:
                x-=1 
                ans.append(x&1)
        return ans