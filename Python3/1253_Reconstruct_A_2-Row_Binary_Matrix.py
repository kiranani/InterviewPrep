class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        n = len(colsum)
        ans0, ans1 = [0] * n, [0] * n
        for i, s in enumerate(colsum):
            if s == 2:
                if lower > 0 and upper > 0:
                    ans0[i], ans1[i] = 1, 1
                    upper, lower = upper - 1, lower - 1
                else:
                    return []
        for i, s in enumerate(colsum):
            if s == 1:
                if upper > 0:
                    ans0[i], upper = 1, upper - 1
                elif lower > 0:
                    ans1[i], lower = 1, lower - 1
                else:
                    return []
        return [ans0, ans1] if lower == upper == 0 else []
        
        
