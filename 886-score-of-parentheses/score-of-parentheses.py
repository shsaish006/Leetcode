class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        return sum (1<<(s[:i].count('(')-s[:i].count(')')-1) for i in range(1,len(s)) if s[i-1:i+1]=='()')
        