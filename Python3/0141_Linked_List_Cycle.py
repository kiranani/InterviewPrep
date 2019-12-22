# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return False
        else:
            slow, fast = head.next, head.next.next
            while slow and fast and fast.next and slow != fast:
                slow, fast = slow.next, fast.next.next
            return slow == fast
        
