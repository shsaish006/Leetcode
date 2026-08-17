class Solution:
    def minCostToMoveChips(self, pos: List[int]) -> int:
        d=[0,0]
        for x in pos:
            d[x%2]+=1 
        return min(d)
        