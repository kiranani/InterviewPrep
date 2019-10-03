# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        last, node = None, head
        while node:
            if node.val < 9:
                last = node
            node = node.next
        if last:
            last.val += 1
        else:
            node = ListNode(1)
            node.next = head
            head, last = node, node
        while last.next:
            last = last.next
            last.val = 0
        return head
        
