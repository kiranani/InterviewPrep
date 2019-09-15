"""
# Definition for a Node.
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next
"""
class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if not head:
            return Node(insertVal, None)
        root = head
        while True:
            if (root.next == head 
                or root.val <= insertVal <= root.next.val 
                or root.next.val < root.val 
                and (insertVal < root.next.val or insertVal > root.val)):
                root.next = Node(insertVal, root.next)
                return head
            root = root.next
        return head
        
