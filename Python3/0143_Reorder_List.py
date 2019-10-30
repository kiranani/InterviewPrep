# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        def split(node):
            slow, fast = node, node.next
            while fast and fast.next:
                slow, fast = slow.next, fast.next.next
            split_head = slow.next
            slow.next = None
            return split_head
        
        def reverse(node):
            if not node or not node.next:
                return node
            prev, head = None, node
            while head:
                temp = head.next
                head.next = prev
                prev, head = head, temp
            return prev
        rev = reverse(split(head))
        while rev:
            t1, t2 = head.next, rev.next
            head.next, rev.next = rev, t1
            head, rev = t1, t2
        
