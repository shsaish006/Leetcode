class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums=sorted(x * x for x in nums)
        m=len(nums)//2
        return sum(nums[m:])-sum(nums[:m])
        