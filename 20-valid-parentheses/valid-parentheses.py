class Solution:
    def isValid(self, s: str) -> bool:
        a=[]
        d={')':'(',']': '[','}':'{'}
        for c in s:
            if c in d:
                if not a or a.pop()!=d[c]:
                    return False 
            else:
                a.append(c)
        return not a
        