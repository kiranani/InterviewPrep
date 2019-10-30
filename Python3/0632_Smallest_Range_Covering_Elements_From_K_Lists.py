class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        if not k:
            return []
        h, ns = [], [len(nums[i]) for i in range(k)]
        mn, mx = float("inf"), -float("inf")
        for i in range(k):
            if ns[i]:
                n = nums[i][0]
                heapq.heappush(h, (n, i, 1))
                mn = min(mn, n)
                mx = max(mx, n)
            else:
                return []
        best, best_m = mx - mn, [mn, mx]
        while len(h) == k:
            _, l, li = heapq.heappop(h)
            if li < ns[l]:
                n = nums[l][li]
                heapq.heappush(h, (n, l, li + 1))
                mn = min(h[0][0], n)
                mx = max(mx, n)
            if mx - mn < best:
                best = mx - mn
                best_m[0], best_m[1] = mn, mx
        return best_m
        
