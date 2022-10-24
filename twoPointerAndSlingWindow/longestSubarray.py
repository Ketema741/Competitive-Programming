class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = res = count = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                count += 1
            if count > 1:
                if nums[left] == 0:
                    count -= 1
                left += 1
            res = max(res, right - left)
            
        return res