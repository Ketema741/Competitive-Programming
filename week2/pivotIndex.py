class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        tot = sum(nums)
        leftSum = 0
        for i in range(len(nums)):
            rightSum = tot - leftSum - nums[i]
            if rightSum == leftSum:
                return i
            leftSum += nums[i]
        return -1
        