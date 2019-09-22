class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        cr, cf = [0] * n, [0] * n
        cr[-1], cf[0] = 1, 1
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                cf[i] = 1 + cf[i - 1]
            else:
                cf[i] = 1
            if ratings[~i] > ratings[~(i - 1)]:
                cf[~i] = 1 + cf[~(i - 1)]
            else:
                cf[~i] = 1
        return sum([max(x, y) for x, y in zip(cr, cf)])
        
