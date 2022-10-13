class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = r =0
        while r !=len(nums)-1:
            if nums[r] != 0:
                r += 1
                l += 1
            while r != len(nums)-1 and nums[r] == 0:
                r += 1
            if l < r and nums[l] == 0:
                tmp = nums[r]
                nums[r] = nums[l]
                nums[l] = tmp
                l += 1
                
                
                
            
        """
        Do not return anything, modify nums in-place instead.
        """
        