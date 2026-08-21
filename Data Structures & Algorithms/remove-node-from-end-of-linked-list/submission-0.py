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
            curr = curr.next
            size += 1

        remove = size - n
        count = 0
        curr = head
        prev = None
        while curr:
            if remove == count:
                if prev is not None:
                    prev.next = curr.next
                    curr.next = None
                else:
                    head = curr.next
                    curr.next = None
                break
            else:
                count += 1
                prev = curr
                curr = curr.next

        
        return head