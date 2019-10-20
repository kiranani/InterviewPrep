from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = list(Counter(tasks).values())
        h = max(counts)
        h_freq = counts.count(h)
        t = (h - 1) * (n + 1) + h_freq
        if t > len(tasks):
            return t
        else:
            return len(tasks)
        
