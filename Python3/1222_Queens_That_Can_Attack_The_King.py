class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        def onBoard(i, j):
            return -1 < i < 8 and -1 < j < 8
        kx, ky = king
        queens = {tuple(x) for x in queens}
        dirs = {"n": (-1, 0), "ne": (-1, 1), "e": (0, 1), "se": (1, 1),
                "s": (1, 0), "sw": (1, -1), "w": (0, -1), "nw": (-1, -1)}
        nei = {k: (kx + v[0], ky + v[1]) for k, v in dirs.items() 
               if onBoard(kx + v[0], ky + v[1])}
        ans = []
        while nei:
            new = {}
            for d, n in nei.items():
                if n in queens:
                    ans.append(list(n))
                else:
                    if onBoard(n[0] + dirs[d][0], n[1] + dirs[d][1]):
                        new[d] = (n[0] + dirs[d][0], n[1] + dirs[d][1])
            nei = new
        return ans
        
