from collections import deque
class Solution:
    def toHexspeak(self, num: str) -> str:
        ans, num = deque(), int(num)
        while num:
            num, rem = divmod(num, 16)
            if rem == 0:
                ans.appendleft("O")
            elif rem == 1:
                ans.appendleft("I")
            elif rem > 9:
                ans.appendleft(chr(55 + rem))
            else:
                return "ERROR"
        return "".join(ans)
        
