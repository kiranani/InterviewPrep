class Solution:
    def similarRGB(self, color: str) -> str:
        h = {10: "aa", 11: "bb", 12: "cc", 13: "dd", 14: "ee", 15: "ff"}
        def getDecimal(c):
            x = 0
            if c[0].isdigit():
                x += 16 * int(c[0])
            else:
                x += 16 * (ord(c[0]) - 87)
            if c[1].isdigit():
                x += int(c[1])
            else:
                x += ord(c[1]) - 87
            return x
        def getClosestHex(d):
            d, m = divmod(d, 17)
            if m > 8:
                d += 1
            if d > 9:
                return h[d]
            else:
                return "{0}{0}".format(d)
                
        r, g, b = getDecimal(color[1:3]), getDecimal(color[3:5]), getDecimal(color[5:])
        print(r,g,b)
        return "#{}{}{}".format(getClosestHex(r), getClosestHex(g), getClosestHex(b))
        
        
