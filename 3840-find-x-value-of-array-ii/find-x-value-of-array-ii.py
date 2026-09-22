# class Solution:
#     def resultArray(self, nums, k, queries):
#         n = len(nums)
#         b = int(n ** .5) + 1
#         m = (n + b - 1) // b
#         p = [1] * m
#         c = [[0] * k for _ in range(m)]
#         def build(x):
#             l, r = x * b, min(n, (x + 1) * b)
#             z = 1
#             c[x] = [0] * k
#             for i in range(l, r):
#                 z = z * nums[i] % k
#                 c[x][z] += 1
#             p[x] = z
#         for i in range(m):
#             build(i)
#         def upd(i, v):
#             nums[i] = v % k
#             build(i // b)
#         def get(s):
#             z = 1
#             d = [0] * k
#             i = s
#             while i < n and i % b:
#                 z = z * nums[i] % k
#                 d[z] += 1
#                 i += 1
#             while i + b <= n:
#                 x = i // b
#                 for j in range(k):
#                     d[z * j % k] += c[x][j]
#                 z = z * p[x] % k
#                 i += b
#             while i < n:
#                 z = z * nums[i] % k
#                 d[z] += 1
#                 i += 1

#             return d
#         ans = []
#         for i, v, s, x in queries:
#             upd(i, v)
#             ans.append(get(s)[x])
#         return ans
class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)
        t = [[1, [0] * k] for _ in range(4 * n)]

        def mg(a, b):
            p, x = a
            q, y = b
            z = x[:]
            for i in range(k):
                z[p * i % k] += y[i]
            return p * q % k, z

        def build(u, l, r):
            if l == r:
                x = nums[l] % k
                t[u] = x, [int(i == x) for i in range(k)]
                return
            m = (l + r) >> 1
            build(u << 1, l, m)
            build(u << 1 | 1, m + 1, r)
            t[u] = mg(t[u << 1], t[u << 1 | 1])

        def upd(u, l, r, x, v):
            if l == r:
                v %= k
                t[u] = v, [int(i == v) for i in range(k)]
                return
            m = (l + r) >> 1
            if x <= m:
                upd(u << 1, l, m, x, v)
            else:
                upd(u << 1 | 1, m + 1, r, x, v)
            t[u] = mg(t[u << 1], t[u << 1 | 1])

        def qry(u, l, r, x):
            if l >= x:
                return t[u]
            m = (l + r) >> 1
            if x <= m:
                return mg(qry(u << 1, l, m, x), t[u << 1 | 1])
            return qry(u << 1 | 1, m + 1, r, x)

        build(1, 0, n - 1)

        ans = []
        for i, v, s, x in queries:
            upd(1, 0, n - 1, i, v)
            ans.append(qry(1, 0, n - 1, s)[1][x])

            

        return ans