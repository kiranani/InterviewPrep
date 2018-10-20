# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        odd, even, firstEven = head, head.next, head.next
        while even is not None and even.next is not None:
            odd.next, even.next = even.next, even.next.next
            odd, even = odd.next, even.next
        odd.next = firstEven
        return head
        
