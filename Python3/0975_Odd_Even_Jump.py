class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        if not A:
            return 0
        n = len(A)
        i_inc = sorted(range(n), key=lambda x: A[x])
        i_dec = sorted(range(n), key=lambda x: -A[x])
        odd_j, even_j = [None] * n, [None] * n
        odd_s, even_s = [], []
        for i in range(n):
            while odd_s and i_inc[i] > odd_s[-1]:
                odd_j[odd_s.pop()] = i_inc[i]
            odd_s.append(i_inc[i])
            while even_s and i_dec[i] > even_s[-1]:
                even_j[even_s.pop()] = i_dec[i]
            even_s.append(i_dec[i])
        c = 1
        valid = [[False, False] for _ in range(n - 1)] + [[True, True]]
        for i in range(n - 2, -1, -1):
            jo, je = odd_j[i], even_j[i]
            if jo is not None:
                valid[i][0] = valid[jo][1]
            if je is not None:
                valid[i][1] = valid[je][0]
            c += +(valid[i][0])
        return c
        
