# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        while fast and fast.next:
            fast.val, fast.next.val = fast.next.val, fast.val
            fast = fast.next.next
        return head