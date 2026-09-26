class Solution:
    def evaluate(self, s: str, knl: list[list[str]]) -> str:
        d=dict(knl)
        a=[]
        i=0 
        while i<len(s):
            if s[i]=='(':
                j=s.find(')',i)
                a.append(d.get(s[i+1:j],'?'))
                i=j+1 
            else:
                a.append(s[i])
                i+=1 
        return ''.join(a)