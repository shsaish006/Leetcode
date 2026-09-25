class Solution:
    def braceExpansionII(self, exp: str) -> list[str]:
        s=exp
        i=0 
        def f():
            nonlocal i 
            a={""}
            while i<len(s) and s[i]!='}':
                if s[i]==',':
                    i+=1 
                    a|=f()
                    return a
                if s[i]=='{':
                    i+=1 
                    b=f()
                    i+=1
                else:
                    j=i 
                    while j<len(s) and s[j].islower():
                        j+=1 
                    b={s[i:j]}
                    i=j 
                a={x+y for x in a for y in b}
            return a 
        return sorted(f())
       