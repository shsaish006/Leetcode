class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        ans=set()
        l=r=0
        for c in s:
            if c=='(': l+=1 
            elif c==')':
                if l: l-=1
                else: r+=1 
        def dfs(i,l,r,b,t):
            if i==len(s):
                if not l and not r and not b: ans.add(t)
                return 
            if l+r>len(s)-i or b<0: return 
            c=s[i]
            if c=='(':
                if l: dfs(i+1,l-1,r,b,t)
                dfs(i+1,l,r,b+1,t+c)
            elif c==')':
                if r: dfs(i+1,l,r-1,b,t)
                if b: dfs(i+1,l,r,b-1,t+c)
            else:
                dfs(i+1,l,r,b,t+c)
        dfs(0,l,r,0,"")
        return list(ans)
        