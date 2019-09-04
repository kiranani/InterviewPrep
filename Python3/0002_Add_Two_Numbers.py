# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def helper(l1, l2, carry):
            rem = 0
            if l1 is None and l2 is None:
                if carry > 0:
                    return ListNode(carry)
                else:
                    return
            elif l1 is None:
                carry, rem = divmod(l2.val + carry, 10)
                l2 = l2.next
            elif l2 is None:
                carry, rem = divmod(l1.val + carry, 10)
                l1 = l1.next
            else:
                carry, rem = divmod(l1.val + l2.val + carry, 10)
                l1, l2 = l1.next, l2.next
            node = ListNode(rem)
            node.next = helper(l1, l2, carry)
            return node
        return helper(l1, l2, 0)
