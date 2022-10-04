class Solution(object):
    def rearrangeArray(self, nums):
        nums_len = len(nums)
        for i in range(1, nums_len-1):
            prev, crnt, nxt = nums[i-1], nums[i], nums[i+1]
            if prev < crnt < nxt or prev > crnt > nxt:
                nums[i], nums[i+1] = nums[i+1], nums[i]
        return nums
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        