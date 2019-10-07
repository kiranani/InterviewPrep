# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        if not head:
            return None
        elif head.next is None:
            return head
        else:
            new_head = self.reverseList(head.next)
            head.next.next = head
            head.next = None
            return new_head
        """
        root, prev = head, None
        while root:
            temp = root.next
            root.next, prev = prev, root
            root = temp
        return prev
        
