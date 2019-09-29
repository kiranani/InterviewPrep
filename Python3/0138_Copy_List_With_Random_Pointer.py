"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        root = head
        while root:
            root.next = Node(root.val, root.next, root.random)
            root = root.next.next
        root, new_head = head, head.next
        while root:
            if root.next.random:
                root.next.random = root.next.random.next
            root = root.next.next
        root = head
        while root:
            if root.next.next:
                temp = root.next.next
                root.next.next = root.next.next.next
                root.next = temp
            else:
                root.next = None
            root = root.next
        return new_head
        
