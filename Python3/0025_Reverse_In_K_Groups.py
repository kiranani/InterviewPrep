# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1:
            return head
        tail, c = head, 0
        while tail is not None and c < k:
            tail = tail.next
            c += 1
        if c < k:
            return head
        last, c, curr, temp = head, 0, head, None
        while c < k:
            curr.next, curr, temp = temp, curr.next, curr
            c += 1
        last.next = self.reverseKGroup(curr, k)
        return temp
