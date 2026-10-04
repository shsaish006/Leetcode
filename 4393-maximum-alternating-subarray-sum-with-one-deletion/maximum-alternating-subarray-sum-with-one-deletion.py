class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        a=b=c=d=-10**14 
        ans=float('-inf')
        for x in nums:
            a,b,c,d=max(x,b+x),a-x,max(a,d+x),max(b,c-x)
            ans=max(ans,a,b,c,d)
        return ans
        