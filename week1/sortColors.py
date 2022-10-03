class Solution(object):
    def sortColors(self, nums):
        occurrence_arr = [0] * 3
        arr_len = len(nums)
        a=0
        for i in range(arr_len):
            occurrence_arr[nums[i]] +=1
        for i in range(3):
            for j in range(occurrence_arr[i]):  
               nums[a] = i
               a+=1
        return nums
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        