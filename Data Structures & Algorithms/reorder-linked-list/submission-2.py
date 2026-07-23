# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        secondHalf = slow.next
        prev = slow.next = None
        while secondHalf:
            nxt = secondHalf.next
            secondHalf.next = prev
            prev = secondHalf
            secondHalf = nxt
        
        first, second = head, prev
        count = 0
        dummy = ListNode()
        tail = dummy
        while second:
            if count % 2 == 0:
                tail.next = first
                first = first.next
            else:
                tail.next = second
                second = second.next
            count += 1
            tail = tail.next
            
        if first:
            tail.next = first
        
        head = dummy.next