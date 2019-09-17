# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head, h = ListNode(None), []
        for i, n in enumerate(lists):
            if n:
                heapq.heappush(h, (n.val, i))
        root = head
        while h:
            i = heapq.heappop(h)[1]
            n = lists[i]
            if n.next:
                heapq.heappush(h, (n.next.val, i))
            root.next, root, lists[i] = n, n, n.next
        return head.next
        
