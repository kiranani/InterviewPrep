class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n, s, m = len(heights), [-1], 0
        for i, h in enumerate(heights):
            while s[-1] != -1 and heights[s[-1]] >= h:
                m = max(m, heights[s.pop()] * (i - s[-1] - 1))
            s.append(i)
        while s[-1] != -1:
            m = max(m, heights[s.pop()] * (n - s[-1] - 1))
        return m
        
        
