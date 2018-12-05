class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        i, j, ma = 0, n - 1, 0
        while i < j:
            mi = height[i] if height[i] < height[j] else height[j]
            w = mi * (j - i)
            ma = ma if ma > w else w
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return ma
        
