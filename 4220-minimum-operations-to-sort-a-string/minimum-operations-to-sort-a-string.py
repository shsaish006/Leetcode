class Solution:
    def minOperations(self, s: str) -> int:
        n=len(s)
        flag=True 
        for i in range(1,n):
            if s[i]<s[i-1]:
                flag=False 
                break 
        if flag:
            return 0 
        if n==2:
            return -1 
        mn=min(s)
        mx=max(s)
        if s[0]==mn or s[n-1]==mx:
            return 1 
        for i in range(1,n-1):
            if s[i]==mn or s[i]==mx:
                return 2 
        return 3
        