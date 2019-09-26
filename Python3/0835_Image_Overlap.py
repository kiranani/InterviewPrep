class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        n, d = len(A), collections.defaultdict(int)
        d[n, n] = 0
        for ai in range(n):
            for aj in range(n):
                if A[ai][aj]:
                    for bi in range(n):
                        for bj in range(n):
                            if B[bi][bj]:
                                d[bi - ai, bj - aj] += 1
        return max(d.values())
        
        
