class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0
        left = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            if k < 0:
                res = max(res, right - left )
                if nums[left] == 0:
                    k += 1
                left += 1
        return right - left + 1

        