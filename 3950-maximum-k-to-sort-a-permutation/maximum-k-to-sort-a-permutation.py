class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        ans=-1 
        for i in range(len(nums)):
            if i!=nums[i]:
                ans&=nums[i]
        return max(ans,0)
        