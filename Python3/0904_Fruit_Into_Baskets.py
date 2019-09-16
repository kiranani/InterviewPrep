class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        l, m, h = 0, 0, collections.defaultdict(int)
        for r, x in enumerate(tree):
            h[x] += 1
            while len(h) > 2:
                if h[tree[l]] == 1:
                    del h[tree[l]]
                else:
                    h[tree[l]] -= 1
                l += 1
            m = max(m, r - l + 1)
        return m
