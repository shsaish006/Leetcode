class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        return sum(len(set(nums[i:j]))**2 for i in range(len(nums)) for j in range(i+1,len(nums)+1))
        