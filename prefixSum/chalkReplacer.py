class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        prefixSum = [0] * len(chalk)
        prefixSum[0] = chalk[0]
        for i in range(1, len(chalk)):
            prefixSum[i] = prefixSum[i-1] + chalk[i]
        remainder = k % prefixSum[-1]
        start, end = 0, len(chalk) - 1
        for i in range(len(prefixSum)):
            mid = start + (end - start) // 2
            if remainder == prefixSum[mid]:
                return mid + 1
            elif remainder < prefixSum[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return start
        