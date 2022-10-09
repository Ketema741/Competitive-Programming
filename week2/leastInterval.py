class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        q = deque()
        times = 0
        while q or maxHeap:
            times +=1 
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, times + n])
            if q and q[0][1] == times:
                heapq.heappush(maxHeap, q.popleft()[0])
        return times
            
        
        