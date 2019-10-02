class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix:
            m, n = len(matrix), len(matrix[0])
            l, r = 0, m * n - 1
            while l <= r:
                mid = (l + r) // 2
                mi, mj = divmod(mid, n)
                if target == matrix[mi][mj]:
                    return True
                elif target < matrix[mi][mj]:
                    r = mid - 1
                else:
                    l = mid + 1
        return False
    
