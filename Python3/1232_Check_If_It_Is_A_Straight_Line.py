class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0, y0 = coordinates[0]
        dx, dy = coordinates[1][0] - x0, coordinates[1][1] - y0
        if dx == 0:
            for x, _ in coordinates[2:]:
                if x0 - x != 0:
                    return False
        elif dy == 0:
            for _, y in coordinates[2:]:
                if y0 - y != 0:
                    return False
        else:
            slope = dy / dx
            for x, y in coordinates[2:]:
                ddx = x - x0
                if ddx == 0 or (y - y0) / ddx != slope:
                    return False
        return True
        
