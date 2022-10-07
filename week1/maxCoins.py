class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        piles = deque(piles)
        sum = 0
        while piles:
            piles.pop()
            sum +=piles.pop()
            piles.popleft()
        return sum 
        