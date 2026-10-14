class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if num*9<sum:
            return ""
        return '9'*(sum//9)+('' if sum%9==0 else str(sum%9))+'0'*(num-(sum+8)//9)
        