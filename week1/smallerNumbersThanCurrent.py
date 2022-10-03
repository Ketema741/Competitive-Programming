class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        nums_len = len(nums)
        count = [0] * nums_len
        for i in range(nums_len):
            for j in range(nums_len):
                if nums[i]>nums[j]:
                    count[i]+=1
        return count

        
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        