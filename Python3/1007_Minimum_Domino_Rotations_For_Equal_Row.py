class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        if not n:
            return -1
        na, nb, sa, sb = A[0], B[0], 0, 0
        for i in range(1, n):
            if A[i] == na:
                pass
            elif B[i] == na:
                sa += 1
            else:
                na = 0
            if B[i] == nb:
                pass
            elif A[i] == nb:
                sb += 1
            else:
                nb = 0
            if not na and not nb:
                return -1
            elif not na:
                na, sa = nb, i + 1 - sb
                if A[i] == B[i]:
                    sa -= 1
            elif not nb:
                nb, sb = na, i + 1 - sa
                if A[i] == B[i]:
                    sb -= 1
        return sa if sa < sb else sb
