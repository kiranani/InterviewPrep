class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        lhs = ""
        if numerator * denominator < 0:
            lhs = "-"
            numerator, denominator = abs(numerator), abs(denominator)
        div, rem = divmod(numerator, denominator)
        lhs += str(div)
        rhs, mods = [], {}
        while rem:
            if rem in mods:
                break
            mods[rem] = len(rhs)
            div, rem = divmod(10 * rem, denominator)
            rhs.append(str(div))
        if rhs and rem:
            return "{}.{}({})".format(
                lhs, "".join(rhs[:mods[rem]]), "".join(rhs[mods[rem]:]))
        elif rhs:
            return "{}.{}".format(lhs, "".join(rhs))
        else:
            return lhs
        
        
