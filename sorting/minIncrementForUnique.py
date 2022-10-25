class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        if not nums: return 0
        nums.sort()
        prev, ans = nums[0], 0
        for i in range(1, len(nums)):
            cur = nums[i]
            if cur <= prev:
                ans += prev - cur + 1
                cur = prev + 1
            prev = cur
        return ans
        