class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        r = len(nums) -1 
        l = 0
        count = 0
        while l < r:
            curr = nums[l] + nums[r]
            if curr == k:
                count += 1
                l+=1
                r-=1
            elif curr < k :
                l+=1
            else:
                r-=1
        return count