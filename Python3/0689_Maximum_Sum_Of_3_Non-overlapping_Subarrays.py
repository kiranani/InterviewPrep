class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        s = sum(nums[:k])
        sums = [s]
        for i, num in enumerate(nums[k:]):
            s += num - nums[i]
            sums.append(s)
        n = len(sums)
        left, right = [0] * n, [0] * n
        l_best, r_best = 0, n - 1
        for i in range(n):
            if sums[i] > sums[l_best]:
                l_best = i
            left[i] = l_best
            ri = n - i - 1
            if sums[ri] >= sums[r_best]:
                r_best = ri
            right[ri] = r_best
        
        best = left[0], k, right[2 * k]
        s_best = sums[best[0]] + sums[best[1]] + sums[best[2]]
        for y in range(k + 1, n - k):
            x, z = left[y - k], right[y + k]
            s = sums[x] + sums[y] + sums[z]
            if s > s_best:
                s_best, best = s, (x, y, z)
        return best
        
