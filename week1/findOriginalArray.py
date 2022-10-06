class Solution(object):
    def findOriginalArray(self, changed):
        changed.sort()
        stk, res = collections.deque([]), []
        for i in changed:
            if stk and stk[0]*2==i:
                b=stk.popleft()
                res.append(b)
            else:
                stk.append(i)
        return res if not stk else []
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        