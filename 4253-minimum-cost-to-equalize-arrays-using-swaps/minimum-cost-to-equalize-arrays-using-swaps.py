class Solution:
    def minCost(self, nums1: list[int], nums2: list[int]) -> int:
        c=Counter(nums1)
        c.subtract(nums2)
        a=[v for v in c.values() if v]
        if any (v%2 for v in a):
            return -1 
        return sum(v for v in a if v>0)//2
