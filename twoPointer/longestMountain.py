class Solution:
    def longestMountain(self, A: List[int]) -> int:
        res, base =  0, 0 
        N = len(A)
        
        while base < N :
            end = base
            if base + 1 < N and A[end] < A[end + 1]:
                while end + 1 < N and A[end]<A[end+1]:
                    end += 1
                if end + 1 < N and A[end] > A[end + 1]:
                    while end + 1< N and A[end]>A[end + 1]:
                        end += 1
                    res = max(res, end - base + 1)
            base = max(end, base + 1)
        return res
                
        