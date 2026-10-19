class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        vals=[]
        for i in range(len(nums)):
            if nums[i]==target:
                vals.append(i)
        return vals
        