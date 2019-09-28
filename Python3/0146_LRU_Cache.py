class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        
class LRUCache:
    def __init__(self, capacity: int):
        self.head = None
        self.tail = None
        self.cap = capacity
        self.count = 0
        self.h = {}
        

    def get(self, key: int) -> int:
        node = self.h.get(key)
        if node:
            self.put(key, node.val)
            return node.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if self.count == 0:
            node, self.count = Node(key, value), 1
            self.head = self.h[key] = self.tail = node
        else:
            node = self.h.get(key)
            if node:
                node.val = value
                if self.count > 1:
                    next_node, prev_node, node.next = node.next, node.prev, None
                    if next_node and prev_node:
                        next_node.prev, prev_node.next = prev_node, next_node
                    elif next_node:
                        self.head, next_node.prev = next_node, None
                    if node != self.tail:
                        self.tail.next, node.prev, self.tail = node, self.tail, node
            else:
                self.count, node = self.count + 1, Node(key, value)
                self.tail.next, node.prev, self.tail = node, self.tail, node
                self.h[key] = node
            if self.count > self.cap:
                node, self.head, self.head.prev = self.head, self.head.next, None
                del self.h[node.key]
                del node
                self.count -= 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
