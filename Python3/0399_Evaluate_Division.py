class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def create_graph(edges, v):
            g = collections.defaultdict(dict)
            for i, edge in enumerate(edges):
                g[edge[0]][edge[1]] = v[i]
                g[edge[1]][edge[0]] = 1 / v[i]
            return g
        def evaluate(s, t, v, g):
            if s not in g or t not in g or s in v: return -1
            if s == t: return 1
            v.add(s)
            for n in g[s]:
                if n not in v:
                    a = evaluate(n, t, v, g)
                    if a > 0:
                        return a * g[s][n]
            v.remove(s)
            return -1
        ans, g = [], create_graph(equations, values)
        for query in queries:
            ans.append(evaluate(query[0], query[1], set(), g))
        return ans
                    
        
