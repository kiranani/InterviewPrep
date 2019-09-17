# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """if l1 and l2:
            if l1.val < l2.val:
                l1.next = self.mergeTwoLists(l1.next, l2)
                return l1
            else:
                l2.next = self.mergeTwoLists(l1, l2.next)
                return l2
        else:
            return l1 or l2"""
        head = ListNode(None)
        root = head
        while l1 and l2:
            if l1.val < l2.val:
                root.next = l1
                l1 = l1.next
            else:
                root.next = l2
                l2 = l2.next
            root = root.next
        root.next = l1 or l2
        return head.next
        
