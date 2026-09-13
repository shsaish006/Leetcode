class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        a=[(i,j) for i in range(len(img1)) for j in range(len(img1)) if img1[i][j]]
        b=[(i,j) for i in range(len(img2)) for j in range(len(img2)) if img2[i][j]]
        cnt={}
        ans=0 
        for i,j in a:
            for h,k in b:
                x=(i-h , j-k)
                cnt[x]=cnt.get(x,0)+1 
                ans=max(ans,cnt[x])
        return ans
        