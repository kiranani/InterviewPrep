# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        else:
            root = head.next
            while root and root.val == head.val:
                root = root.next
            head.next = root
            self.deleteDuplicates(root)
            return head
        
