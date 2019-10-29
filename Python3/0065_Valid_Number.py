class Solution:
    def isNumber(self, s: str) -> bool:
        s, signs = s.strip(), ["+", "-"]
        has_digit = has_dot = has_e = has_sign = False
        for c in s:
            if c.isdigit():
                has_digit = True
            elif c == ".":
                if has_dot or has_e:
                    return False
                has_dot = True
            elif c == "e":
                if not has_digit or has_e:
                    return False
                has_e, has_sign, has_digit, has_dot = True, False, False, False
            elif c in signs:
                if has_digit or has_sign or (not has_digit and has_dot):
                    return False
                has_sign = True
            else:
                return False
        return has_digit
        
        
