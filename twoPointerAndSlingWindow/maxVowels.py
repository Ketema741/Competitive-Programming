class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left = res = vCount = 0
        v = 'aeuio'
        for right in range(len(s)):
            if s[right] in v:
                vCount += 1
            if (right - left + 1) == k :
                res = max(res, vCount)
                if s[left] in v:
                    vCount -= 1
                left += 1
        return res