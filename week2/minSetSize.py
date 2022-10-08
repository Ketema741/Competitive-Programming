class Solution:
    def minSetSize(self, arr: List[int]) -> int: 
        half = len(arr)//2
        count = 0
        cnt = Counter(arr)
        cnt = sorted(cnt.values(),reverse=True)
        
        while half>0:
            half -= cnt[count]
            count += 1
        return count
            
        