class Solution(object):
    def kClosest(self, points, k):
        points.sort(key= lambda x: x[0]**2 + x[1]**2)
        closest_arr = []
        for i in range(k):
            closest_arr.append(points[i])
        return closest_arr
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        