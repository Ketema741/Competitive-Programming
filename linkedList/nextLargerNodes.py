# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        values = []
        while head:
            values.append(head.val)
            head = head.next
        res = [0]*len(values)
        stack = []
        for i, value in enumerate(values):
            while stack and values[stack[-1]] < value:
                smaller = stack.pop()
                res[smaller] = value
            stack.append(i)
        return res
        