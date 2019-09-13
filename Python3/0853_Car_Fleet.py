class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        if not n:
            return 0
        sorted_i = sorted(range(n), key=lambda x: target - position[x])
        c, t = 1, (target - position[sorted_i[0]]) / speed[sorted_i[0]]
        for i in sorted_i[1:]:
            ti = (target - position[i]) / speed[i]
            if ti > t:
                c, t = c + 1, ti
        return c
