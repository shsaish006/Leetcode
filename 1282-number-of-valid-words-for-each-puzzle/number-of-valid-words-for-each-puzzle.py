class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        from collections import Counter 
        c=Counter(sum(1<<(ord(x)-97) for x in set(w)) for w in words)
        ans=[]
        for p in puzzles:
            m=sum(1<<(ord(x)-97) for x in set(p))
            f=1<<(ord(p[0])-97)
            z=0
            x=m 
            while x:
                if x&f:
                    z+=c[x]
                x=(x-1)&m 
            ans.append(z)
        return ans
        