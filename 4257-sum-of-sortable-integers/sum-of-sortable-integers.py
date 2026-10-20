from itertools import count
from math import isqrt
class Solution:
    def sortableIntegers(self,nums):
        n=len(nums)
        prefMax=[0]*(n+1)



        
        suffMin=[10**9]*(n+1)
        prefDrop=[0]*n
        for i in range(n):
            prefMax[i+1]=max(prefMax[i],nums[i])
        for i in range(n-1,-1,-1):
            suffMin[i]=min(nums[i],suffMin[i+1])
        for i in range(1,n):
            prefDrop[i]=prefDrop[i-1]+(nums[i-1]>nums[i])
        ans=0
        for i in count(1):
            if i>isqrt(n):
                break
            if n%i==0:
                for k in (i,n//i):
                    flag=True
                    for idx in range(0,n,k):
                        nxt=idx+k-1
                        cnt=prefDrop[nxt]-prefDrop[idx]
                        if nums[nxt]>nums[idx]:
                            cnt+=1
                        if cnt>1 or prefMax[idx]>suffMin[idx]:
                            flag=False
                            break
                    if flag:
                        ans+=k
                    if i==n//i:
                        break
        return ans