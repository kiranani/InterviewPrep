class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n, ans, seen = len(nums), [], set()
        def recurse(arr):
            if len(arr) == n:
                ans.append(arr)
                return
            for num in nums:
                if num not in seen:
                    seen.add(num)
                    recurse(arr + [num])
                    seen.remove(num)
        recurse([])
        return ans
        
