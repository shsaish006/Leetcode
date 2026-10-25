class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        hh=(nums,minK,maxK)
        # ans=left=mini=maxi=0 
        ans=left=0
        for i,x in enumerate(nums):
            if not minK <=x <=maxK:
                left=i+1 
            ans+=i-left+1
            # if x==minK:
            #     mini=i+1 
            # if x==maxK:
            #     maxi=i+1 
            # ans+=max(0,min(mini,maxi)-left+1)
        return ans