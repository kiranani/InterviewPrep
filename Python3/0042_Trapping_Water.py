class Solution:
    def trap(self, height):
        n, total, prev, high, acc, maxH = len(height), 0, 0, 0, 0, 0
        if n == 0:
            return 0
        for h in height:
            if h >= high:
                total += acc
                maxH, high, acc = h, h, 0
            else:
                acc += high - h
        high, acc = 0, 0
        for i in range(n - 1, -1, -1):
            if height[i] >= high:
                total += acc
                high, acc = height[i], 0
                if high == maxH:
                    return total
            else:
                acc += high - height[i]
        return total
        
