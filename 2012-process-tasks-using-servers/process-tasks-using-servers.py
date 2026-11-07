from heapq import *
class Solution:
    def assignTasks(self, servers, tasks):
        free = [(w, i) for i, w in enumerate(servers)]
        busy, ans = [], []
        heapify(free)
        for i, t in enumerate(tasks):
            while busy and busy[0][0] <= i:
                s, w, idx = heappop(busy)
                heappush(free, (w, idx))
            if free:
                w, idx = heappop(free)
                heappush(busy, (i + t, w, idx))
            else:
                s, w, idx = heappop(busy)
                heappush(busy, (s + t, w, idx))
            ans.append(idx)
        return ans