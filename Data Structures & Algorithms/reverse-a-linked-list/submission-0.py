# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        l = []
        
        value = head
        while value:
            l.append(value.val)
            value = value.next

        count = len(l) - 1
        curr = head
        while curr:
            curr.val = l[count]
            count -= 1
            curr = curr.next
        
        return head