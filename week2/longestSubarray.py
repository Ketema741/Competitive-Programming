class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        dqMin, dqMax = deque(), deque()
        l, ans = 0, 0
        for r in range(len(nums)):
            while dqMin and nums[dqMin[-1]] >= nums[r]:
                dqMin.pop()
            while dqMax and nums[dqMax[-1]] <= nums[r]:
                dqMax.pop()
            dqMin.append(r)
            dqMax.append(r)
            while nums[dqMax[0]] -nums[dqMin[0]] > limit:
                l += 1
                if dqMin[0] < l: dqMin.popleft()
                if dqMax[0] < l: dqMax.popleft()
            ans = max(ans, r - l + 1)
        return ans
            
            