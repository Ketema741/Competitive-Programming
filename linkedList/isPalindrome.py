# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cur = head
        arr = []
        while cur:
            arr.append(cur.val)
            cur = cur.next
        return arr == arr[::-1]