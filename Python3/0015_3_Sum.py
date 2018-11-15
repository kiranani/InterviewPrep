class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans, seen = set(), set()
        for i, v in enumerate(nums[:-2]):
            if v in seen:
                continue
            seen.add(v)
            s = set()
            for x in nums[i + 1:]:
                if x not in s:
                    s.add(-v - x)
                else:
                    ans.add((v, -v-x, x))
        return [list(x) for x in ans]
