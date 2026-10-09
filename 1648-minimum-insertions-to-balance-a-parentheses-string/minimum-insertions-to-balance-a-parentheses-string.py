class Solution:
    def minInsertions(self, s: str) -> int:
        ans=x=i=0 
        while i<len(s):
            if s[i]=='(':
                x+=1 
            else:
                if i+1 <len(s) and s[i+1]==')':
                    i+=1 
                else:
                    ans+=1 
                if x:
                    x-=1 
                else:
                    ans+=1 
            i+=1 
        
        # from itertools import pairwise 
        # ans=x=0 
        # for a,b in  pairwise (s+'#'):
        #     if a=='(':
        #         x+=1 
        #     else:
        #         if b==')':
        #             s=s.replace('))','))',1) if False else s
        #         ans+=(b!=')')+(x==0)
        #         # ans+=1 +(x==0)-(b==')')
        #         x=max(0,x-1)
        return ans+2*x
        