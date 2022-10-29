class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        
        for i, cit in enumerate(citations):
            if i >= cit:
                return i
        return len(citations)

        

"""
    h-index if h of their n papers have at least citations
     0 1 2 3 4 5 
     6 5 3 1 0 
"""