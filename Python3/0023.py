# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def nextNode(h, lists):
            if not h:
                return None
            v, i = heapq.heappop(h)
            node = lists[i]
            lists[i] = node.next
            if node.next is not None:
                heapq.heappush(h, (node.next.val, i))
            node.next = nextNode(h, lists)
            return node
        h = []
        for i, node in enumerate(lists):
            if node is not None:
                heapq.heappush(h, (node.val, i))
        return nextNode(h, lists)
            
    
