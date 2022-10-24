class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        N = len(cardPoints)
        total = sum(cardPoints[N-k:])
        left, right = 0, N - k
        res = total
        while right < N:
            total += (cardPoints[left] - cardPoints[right])
            res = max(res, total)
            left += 1
            right += 1
        return res
        