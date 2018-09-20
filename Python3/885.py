class Solution:
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        dh = {0: "E", 1: "S", 2: "W", 3: "N"}
        rr, cc = {x: 1 for x in range(R)}, {x: 1 for x in range(C)}
        j, d, l = 1, 0, [[r0, c0]]
        while len(l) < R * C:
            j += 1
            inc = j // 2
            if dh[d] == "E":
                for i in range(inc):
                    c0 += 1
                    if rr.get(r0) and cc.get(c0):
                        l.append([r0, c0])
                d = (d + 1) % 4
                #print(j, inc, l)
            elif dh[d] == "S":
                for i in range(inc):
                    r0 += 1
                    if rr.get(r0) and cc.get(c0):
                        l.append([r0, c0])
                d = (d + 1) % 4
                #print(j, inc, l)
            elif dh[d] == "W":
                for i in range(inc):
                    c0 -= 1
                    if rr.get(r0) and cc.get(c0):
                        l.append([r0, c0])
                d = (d + 1) % 4
                #print(j, inc, l)
            elif dh[d] == "N":
                for i in range(inc):
                    r0 -= 1
                    if rr.get(r0) and cc.get(c0):
                        l.append([r0, c0])
                d = (d + 1) % 4
                #print(j, inc, l)
        return l
