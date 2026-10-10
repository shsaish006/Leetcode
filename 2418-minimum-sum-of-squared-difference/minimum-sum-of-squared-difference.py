from itertools import accumulate
from bisect import bisect_left
class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        d = sorted([abs(a - b) for a, b in zip(nums1, nums2)], reverse=True)
        k = k1 + k2
        n = len(d)
        if sum(d) <= k:
            return 0
        d = list(accumulate(d))
        i = bisect_left([d[j] - (j + 1) * d[j] // (j + 1) for j in range(n)], k)
        l, r = 0, max(nums1 + nums2)
        while l < r:
            m = (l + r) // 2
            if sum(max(abs(a - b) - m, 0) for a, b in zip(nums1, nums2)) <= k:
                r = m
            else:
                l = m + 1
        k -= sum(max(abs(a - b) - l, 0) for a, b in zip(nums1, nums2))
        d = [min(abs(a - b), l) for a, b in zip(nums1, nums2)]
        for i in range(n):
            if k and d[i] == l:
                d[i] -= 1
                k -= 1

        return sum(v * v for v in d)