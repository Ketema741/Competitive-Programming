class HeapWord:
    def __init__(self, word, count):
        self.word = word
        self.count = count
            
    def __gt__(self, other):
        if self.count > other.count:
            return True
        
        elif self.count < other.count:
            return False
        
        for s, o in zip_longest(self.word, other.word, fillvalue='#'):
            # if a letter is '#', that means it is smaller that the other word,
            # and therefore is GREATER
            if s < o or s == '#':
                return True 
            elif s > o or o == "#":
                return False      


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        heap = []
        
        for w, count in counter.items():
            word = HeapWord(w, count)
            
            if len(heap) < k:
                heapq.heappush(heap, word)
                
            elif word > heap[0]:
                heapq.heapreplace(heap, word)
                    
        return [w.word for w in sorted(heap, reverse=True)]