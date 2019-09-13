class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        n = len(words1)
        if n != len(words2):
            return False
        g = collections.defaultdict(set)
        for pair in pairs:
            g[pair[0]].add(pair[1])
            g[pair[1]].add(pair[0])
        def dfs(s, d, v):
            if d in g[s] or s == d:
                return True
            elif not g[s] or s in v:
                return False
            v.add(s)
            for c in g[s]:
                if dfs(c, d, v):
                    return True
            return False
        for i in range(n):
            if not dfs(words1[i], words2[i], set()):
                return False
            else:
                g[words1[i]].add(words2[i])
                g[words2[i]].add(words1[i])
        return True
        
        
