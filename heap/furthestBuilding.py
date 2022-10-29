class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        pq = []
        n = len(heights)
        
        for i in range(n-1):
            diff = heights[i+1] - heights[i]
            if diff > 0:
                heapq.heappush(pq, diff)
            if len(pq) > ladders:
                bricks = bricks-heapq.heappop(pq)
            if bricks < 0:
                return i
        
        return n-1