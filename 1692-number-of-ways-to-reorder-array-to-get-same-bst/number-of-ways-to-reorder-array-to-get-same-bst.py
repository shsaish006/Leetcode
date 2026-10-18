class Solution:
    def numOfWays(self, nums):
        from math import comb

        def dfs(nums):
            if len(nums) < 3:
                return 1
            left = [x for x in nums if x < nums[0]]
            right = [x for x in nums if x > nums[0]]
            return comb(len(left) + len(right), len(left)) * dfs(left) * dfs(right) % (10**9 + 7)

        return (dfs(nums) - 1) % (10**9 + 7)