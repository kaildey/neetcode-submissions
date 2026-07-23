# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        check = False
        for i in range(len(lists)):
            tail = dummy

            if lists[i]:
                if not check:
                    tail.next = lists[i]
                    check = True
                else:
                    node = lists[i]
                    prev = tail.next
                    while prev and node:
                        if prev.val <= node.val:
                            tail.next = prev
                            prev = prev.next
                        else:
                            tail.next = node
                            node = node.next
                        tail = tail.next

                    if prev:
                        tail.next = prev
                    if node:
                        tail.next = node

        return dummy.next 