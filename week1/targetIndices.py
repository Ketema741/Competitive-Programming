class Solution(object):
    def targetIndices(self, nums, target):
        sorted_nums = sorted(nums)
        target_indeces = []
        for i in range(len(nums)):
            if sorted_nums[i] == target:
                target_indeces.append(i)
        return target_indeces
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """