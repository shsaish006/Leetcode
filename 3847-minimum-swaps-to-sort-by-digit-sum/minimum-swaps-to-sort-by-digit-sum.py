class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n=len(nums)
        arr=sorted((sum(map(int,str(x))),x) for x in nums)
        d={x : i for i,(_, x) in enumerate(arr)}
        cvr=[0]*n 
        ans=0 
        for i in range(n):
            if cvr[i]:
                continue 
            j=i 
            cnt=0 
            while not cvr[j]:
                cvr[j]=1 
                j=d[nums[j]]
                cnt+=1 
            ans+=cnt-1
        return ans
        