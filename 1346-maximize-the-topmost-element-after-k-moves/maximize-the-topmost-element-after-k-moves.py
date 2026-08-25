class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        n=len(nums)
        if not k: return nums[0]
        if n==1 : return -1 if k&1 else nums[0]
        return max(nums[:k-1]+nums[k:k+1],default=-1)
        