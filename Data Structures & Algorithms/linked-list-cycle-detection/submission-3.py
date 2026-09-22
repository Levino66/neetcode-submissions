# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        f = None
        if head:
            s = head
            f = head.next
        
        while f and f.next:
            if s == f:
                return True
            f = f.next.next
            s = s.next
        return False


