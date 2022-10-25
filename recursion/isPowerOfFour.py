class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        check = 1
        while n >= check:
            if n == check: return True
            check *= 4
        return False
        