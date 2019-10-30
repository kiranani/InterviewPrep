class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        n1, n2 = len(A), len(B)
        if not n1 or not n2:
            return []
        def findIntersection(int1, int2):
            left, right = max(int1[0], int2[0]), min(int1[1], int2[1])
            if left <= right:
                return [left, right]
        i1, i2, ans = 0, 0, []
        while i1 < n1 and i2 < n2:
            inter = findIntersection(A[i1], B[i2])
            if inter:
                ans.append(inter)
            if A[i1][1] < B[i2][1]:
                i1 += 1
            elif A[i1][1] > B[i2][1]:
                i2 += 1
            else:
                i1 += 1
                i2 += 1
        return ans
        
        
