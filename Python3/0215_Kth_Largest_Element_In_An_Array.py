class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        k = n - k
        def partition(l, r, p):
            nums[r], nums[p] = nums[p], nums[r]
            si = l
            for i in range(l, r):
                if nums[i] < nums[r]:
                    nums[i], nums[si] = nums[si], nums[i]
                    si += 1
            nums[r], nums[si] = nums[si], nums[r]
            return si
        def helper(l, r):
            if l == r:
                return nums[l]
            p = random.randint(l, r)
            p = partition(l, r, p)
            if p == k:
                return nums[k]
            elif p < k:
                return helper(p + 1, r)
            else:
                return helper(l, p - 1)  
        return helper(0, n - 1)
        
