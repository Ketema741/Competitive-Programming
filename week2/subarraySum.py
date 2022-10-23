class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prefixSum = {0:1}
        curSum = 0
        
        for i in nums:
            curSum += i
            diff = curSum - k 
            res += prefixSum.get(diff, 0)
            prefixSum[curSum] = 1 + prefixSum.get(curSum, 0)
        return res 
    
   