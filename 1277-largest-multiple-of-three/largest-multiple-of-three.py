class Solution:
    def largestMultipleOfThree(self, dig: List[int]) -> str:
        dig.sort(reverse=True)
        s=sum(dig)%3 
        if s:
            a=[x for x in dig if x%3==s]
            if a:
                dig.remove(a[-1])
            else:
                a=[x for x in dig if x%3!=0 and x%3!=s]
                if len(a)<2: return ""
                dig.remove(a[-1])
                dig.remove(a[-2])
        if not dig: return ""
        if dig[0]==0: return "0"
        return ''.join(map(str,dig))
        # return ''.join(map(str,dig)) if any(dig) else "0"

        