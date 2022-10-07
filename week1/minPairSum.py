class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        nums = deque(nums)
        mx = []
        while nums:
            r = nums.pop()
            l = nums.popleft()
            mx.append(l+r)
        return max(mx[:])
            