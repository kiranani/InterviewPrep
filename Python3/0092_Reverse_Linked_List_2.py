# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m >= n or not head or not head.next:
            return head
        c, root, prev = 1, head, None
        while root and c < m:
            prev, root, c = root, root.next, c + 1
        rhead, rprev = root, None
        while root and c <= n:
            temp = root.next
            root.next, rprev = rprev, root
            root, c = temp, c + 1
        rhead.next = root
        if prev:
            prev.next = rprev
        else:
            return rprev
        return head
        
        
