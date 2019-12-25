from random import uniform
from math import sin, cos, pi
class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r_2, self.p_2 = radius ** 2, 2 * pi
        self.x, self.y = x_center, y_center

    def randPoint(self) -> List[float]:
        r = uniform(0, self.r_2) ** 0.5
        t = uniform(0, self.p_2)
        return [self.x + r * sin(t), self.y + r * cos(t)]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
