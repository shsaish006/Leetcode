class Solution:
    def peakValleyDifference(self, nums: list[int]) -> int:
        return sum(nums[i] if nums[i]> nums[i-1] and nums[i]> nums[i+1] else -nums[i] if nums[i]<nums[i-1] and nums[i]<nums[i+1] else 0 for i in range(1,len(nums)-1))
        