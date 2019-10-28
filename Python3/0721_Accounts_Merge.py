class DisjointSetUnion:
    def __init__(self):
        self.par = {}
    def find(self, e):
        if e not in self.par:
            self.par[e] = e
        if e != self.par[e]:
            self.par[e] = self.find(self.par[e])
        return self.par[e]
    def union(self, e1, e2, m):
        p1, p2 = self.find(e1), self.find(e2)
        if p1 in m:
            self.par[p2] = p1
        else:
            self.par[p1] = p2
            
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu, h, e = DisjointSetUnion(), {}, set()
        for account in accounts:
            h[account[1]] = account[0]
            e.add(account[1])
            for email in account[2:]:
                e.add(email)
                dsu.union(account[1], email, h)
        m = collections.defaultdict(list)
        for email in e:
            m[dsu.find(email)].append(email)
        return [[h[k]] + sorted(v) for k, v in m.items()]
        
