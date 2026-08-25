class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        from bisect import bisect_left 
        nums.sort()
        l,r=0,nums[-1]-nums[0]
        while l<r:
            m=(l+r)//2 
            c=0 
            for i,x in enumerate(nums):
                c+=i-bisect_left(nums,x-m,0,i)
            if c>=k:
                r=m 
            else:
                l=m+1
        return l        