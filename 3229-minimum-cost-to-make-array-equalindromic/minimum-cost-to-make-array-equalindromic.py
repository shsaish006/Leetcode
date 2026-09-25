class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        nums.sort()
        p=lambda x:str (x)==str(x)[::-1]
        l=r=nums[len(nums)//2]
        while not p(l): l-=1 
        while not p(r): r+=1
        return min(sum(abs(x-l) for x in nums),sum(abs(x-r) for x in nums))
