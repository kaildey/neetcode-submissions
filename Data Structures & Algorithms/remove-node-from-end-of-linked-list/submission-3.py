# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next
        
        stop = size - n + 1
        cnt = 1

        curr = head
        dummy = ListNode()
        prev = dummy
        while stop - cnt > 0:
            prev.next = curr
            curr = curr.next
            prev = prev.next
            cnt += 1
        
        if curr:
            prev.next = curr.next
        
        return dummy.next