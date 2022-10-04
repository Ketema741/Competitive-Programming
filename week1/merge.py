class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        non_overlapp = [intervals[0]]
        for i in intervals:
            if non_overlapp[-1][1]>= i[0]:
                non_overlapp[-1][1] = max(non_overlapp[-1][1],i[1])
            else:
                non_overlapp.append(i)
        return non_overlapp
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        