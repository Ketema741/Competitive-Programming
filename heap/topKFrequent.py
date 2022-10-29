class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = Counter(nums)
        nums = list(nums.items())
        srt = sorted(nums, key=lambda kv:(kv[1],kv[0]), reverse=True)
        ans = []
        x = 0
        while k!=x:
            ans.append(srt[x][0])
            x+=1
        return ans
        