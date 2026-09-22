# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2

        if not list2:
            return list1

        curr1 = list1
        curr2 = list2

        if curr1.val < curr2.val:
            prev = head = curr1
            curr1 = curr1.next
        else:
            prev = head = curr2
            curr2 = curr2.next

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                prev.next = curr1
                prev = curr1
                curr1 = curr1.next
            else:
                prev.next = curr2
                prev = curr2
                curr2 = curr2.next
        
        while curr1:
            prev.next = prev = curr1
            curr1 = curr1.next
        
        while curr2:
            prev.next = prev = curr2
            curr2 = curr2.next

        return head

        