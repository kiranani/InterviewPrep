from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r, c, g = defaultdict(set), defaultdict(set), defaultdict(set)
        for i in range(9):
            for j in range(9):
                char, k = board[i][j], 3 * (i // 3) + j // 3
                if char != ".":
                    if char in r[i] or char in c[j] or char in g[k]:
                        return False
                    r[i].add(char)
                    c[j].add(char)
                    g[k].add(char)
        return True
        
