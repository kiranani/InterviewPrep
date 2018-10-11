class Solution:
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        def convertToInt(x):
            if x[0] == "-":
                if x[-1] == "i":
                    return -int(x[1:-1])
                else:
                    return -int(x[1:])
            else:
                if x[-1] == "i":
                    return int(x[:-1])
                else:
                    return int(x)

        aR, aI = a.split("+")
        bR, bI = b.split("+")
        aR, aI, bR, bI = convertToInt(aR), convertToInt(aI), convertToInt(bR), convertToInt(bI)
        r = aR * bR - aI * bI
        i = aR * bI + bR * aI
        return str(r) + "+" + str(i) + "i"
