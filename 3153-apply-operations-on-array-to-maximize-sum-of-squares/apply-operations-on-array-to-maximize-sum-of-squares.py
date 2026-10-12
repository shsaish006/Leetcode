class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        cnt=[sum(x>> i & 1 for x in nums) for i in range(31)]
        ans=0 
        for _ in range(k):
            x=sum((cnt[i]>0)<<i for i in range(31))
            cnt=[c-(c>0) for c in cnt]
            ans=(ans+x*x)%(10**9+7)
        return ans
        