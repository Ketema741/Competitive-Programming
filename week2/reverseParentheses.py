class Solution:
    def reverseParentheses(self, s: str) -> str:
        while "(" in s:
            open_index = 0
            for i in range(len(s)):
                if s[i] == "(":
                    open_index = i
                elif s[i] == ")":
                    s = s.replace(s[open_index:i+1], s[open_index+1: i][::-1])
                    break
        return s
        