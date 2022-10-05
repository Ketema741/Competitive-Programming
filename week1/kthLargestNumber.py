class Solution(object):
    def kthLargestNumber(self, nums, k):
        rev =  list(map(int, nums))
        rev.sort(reverse=True)
        return str(rev[k-1])
            
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        