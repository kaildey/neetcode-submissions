# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        li = []
        curr = head

        while curr:
            li.append(curr.val)
            curr = curr.next
        
        li2 = []
        l, r = 0, len(li) - 1
        count = 0
        while count != len(li):
            if count % 2 == 0:
                li2.append(li[l])
                l += 1
            else:
                li2.append(li[r])
                r -= 1
            count += 1

        curr = head
        count = 0
        while curr:
            curr.val = li2[count]
            count += 1
            curr = curr.next

        return curr