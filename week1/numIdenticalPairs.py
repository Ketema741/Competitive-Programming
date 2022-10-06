class Solution(object):
    def numIdenticalPairs(self, nums):
        count = 0
        for i in range (len(nums)):
            for j in range (1, len(nums)):
                if nums[i] == nums[j] and i<j:
                    count += 1
        return count
        """
        :type nums: List[int]
        :rtype: int
        """
        