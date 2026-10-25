class Solution:
    def countMagicalPairs(self, s: str) -> int:
        ans=0 
        for j in range(len(s)-1):
            cnt,st=defaultdict(int),set()
            for i in range(j,-1,-1):
                st.add(s[i])
                cnt[len(st)]+=1 
            st=set()
            for k in range(j+1,len(s)):
                st.add(s[k])
                ans+=cnt[len(st)]
        return ans
        