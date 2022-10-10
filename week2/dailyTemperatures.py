class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        stack = []
        for i,v in enumerate(temperatures):
            while stack and v > temperatures[stack[-1]]:
                left = stack.pop()
                ans[left] = i-left
            stack.append(i)
        return ans
