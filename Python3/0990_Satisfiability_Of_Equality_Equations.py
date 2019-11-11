class DisjointSetUnion:
    def __init__(self):
        self.par = {}
        
    def find(self, node):
        if node not in self.par:
            self.par[node] = node
        elif node != self.par[node]:
            self.par[node] = self.find(self.par[node])
        return self.par[node]
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 != p2:
            self.par[p2] = p1
    
    def are_disjoint(self, n1, n2):
        return self.find(n1) != self.find(n2)
            
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        ineq, dsu = [], DisjointSetUnion()
        for eq in equations:
            if eq[1] == "=":
                dsu.union(eq[0], eq[3])
            else:
                ineq.append((eq[0], eq[3]))
        for v1, v2 in ineq:
            if not dsu.are_disjoint(v1, v2):
                return False
        return True
        
        
