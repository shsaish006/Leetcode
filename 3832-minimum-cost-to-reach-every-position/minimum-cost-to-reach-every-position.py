class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        return [min(cost[:i+1]) for i in range(len(cost))]
        