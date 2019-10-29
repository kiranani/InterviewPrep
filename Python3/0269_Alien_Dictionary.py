from collections import defaultdict
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        n = len(words)
        graph, degrees = defaultdict(set), defaultdict(int)
        for i in range(n):
            for c in words[i]:
                degrees[c]
            if i > 0:
                word1, word2 = words[i - 1], words[i]
                l1, l2 = len(word1), len(word2)
                j, l = 0, min(l1, l2)
                while j < l:
                    c1, c2 = word1[j], word2[j]
                    if c1 != c2:
                        if c1 in graph[c2]:
                            return ""
                        elif c2 not in graph[c1]:
                            graph[c1].add(c2)
                            degrees[c2] += 1
                        break
                    j += 1
                if j == l and l1 > l:
                    return ""
        ans = []
        while True:
            q = [c for c in degrees if not degrees[c]]
            if not q:
                break
            for c in q:
                del degrees[c]
                ans.append(c)
                for ch in graph[c]:
                    degrees[ch] -= 1
        if degrees:
            return ""
        else:
            return "".join(ans)
                    
        
