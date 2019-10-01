class DisjointSetUnion:
    def __init__(self, n):
        self.rank = [0] * n
        self.parents = list(range(n))
    
    def union(self, node1, node2):
        parent1, parent2 = self.find(node1), self.find(node2)
        if parent1 == parent2:
            return False
        elif self.rank[parent1] < self.rank[parent2]:
            self.parents[parent1] = parent2
        elif self.rank[parent1] > self.rank[parent2]:
            self.parents[parent2] = parent1
        else:
            self.parents[parent2] = parent1
            self.rank[parent1] += 1
        return True
    
    def find(self, node):
        if node != self.parents[node]:
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        graph = DisjointSetUnion(n)
        for edge in edges:
            if not graph.union(*edge):
                return False
        return len(edges) == n - 1
        
