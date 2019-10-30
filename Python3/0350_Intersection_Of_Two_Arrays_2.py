from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1, ans = Counter(nums1), []
        for num in nums2:
            if c1[num]:
                c1[num] -= 1
                ans.append(num)
        return ans
        
