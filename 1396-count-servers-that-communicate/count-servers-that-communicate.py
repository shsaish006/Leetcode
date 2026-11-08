class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        r=list(map(sum,grid))
        c=list(map(sum,zip(*grid)))
        return sum(x and (r[i]>1 or c[j]>1) for i,row in enumerate(grid) for j,x in enumerate(row))
        