class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        if not A:
            return 0
        m, n, ri = len(A), len(A[0]), set()
        def dc(ind, l, r):
            if ind >= n:
                return
            elif ind in ri:
                dc(ind + 1, l, r)
            removed, inc = False, True
            for i in range(l, r):                
                if A[i][ind] > A[i + 1][ind]:
                    ri.add(ind)
                    removed = True
                    break
                elif A[i][ind] == A[i + 1][ind]:
                    inc = False
            if not removed and not inc:
                d = collections.defaultdict(list)
                for i in range(l, r + 1):
                    d[A[i][ind]].append(i)
                for k in d:
                    if len(d[k]) > 1:
                        dc(ind + 1, d[k][0], d[k][-1])
            elif removed:
                dc(ind + 1, l, r)                    
            
        dc(0, 0, m - 1)
        return len(ri)
