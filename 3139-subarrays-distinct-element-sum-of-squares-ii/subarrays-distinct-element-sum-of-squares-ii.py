class BIT:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 2)

    def add(self, i, val):
        i += 1
        while i <= self.n:
            self.tree[i] += val
            i += i & -i

    def query(self, i):
        i += 1
        curr = 0
        while i > 0:
            curr += self.tree[i]
            i -= i & -i
        return curr

class Solution:
    def sumCounts(self, A: List[int]) -> int:
        mod = 10**9 + 7
        n = len(A)
        bit1 = BIT(n + 2)
        bit2 = BIT(n + 2)
        nums = {}
        curr = tot = 0

        def add(left, right, val):
            bit1.add(left, val)
            bit1.add(right + 1, -val)
            bit2.add(left, left * val)
            bit2.add(right + 1, -(right + 1) * val)

        def query(i):
            return (i + 1) * bit1.query(i) - bit2.query(i)

        for i, val in enumerate(A):
            j = nums.get(val, -1) + 1
            q = query(i) - query(j - 1)
            curr = (curr + 2 * q + i - j + 1) % mod
            tot = (tot + curr) % mod
            add(j, i, 1)
            nums[val] = i

        return tot