class Solution:
    def trap(self, height):
        total = 0
        prev = 0
        can = 0
        Max = 0
        for i in height:
            if i >= prev:
                total += can
                can = 0
                prev = i
                Max = i
            else:
                can += prev - i
        prev = 0
        can = 0
        height = height[::-1]
        for i in height:
            if i >= prev:
                total += can
                can = 0
                prev = i
                if i == Max:
                    break
            else:
                can += prev - i
        return total
