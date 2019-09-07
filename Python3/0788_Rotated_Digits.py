class Solution(object):
    def rotatedDigits(self, N):
        c = 0
        b, g = {"3", "4", "7"}, {"2", "5", "6", "9"}
        for i in range(1, N + 1):
            n = set(str(i))
            if not n.intersection(b) and n.intersection(g):
                c += 1
        return c
