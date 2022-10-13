# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = dummy = ListNode() 
        l.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head.next != None and head.val == head.next.val:
                    head = head.next
                head = head.next
                l.next = head
            else:
                head = head.next
                l = l.next
        return dummy.next
                