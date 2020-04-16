class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        f, z = 0, 1
        for bed in flowerbed:
            if not bed:
                z += 1
            else:
                if z > 1:
                    f += (z - 1) // 2
                z = 0
            if f >= n:
                return True
        if z > 1:
            f += z // 2
        return f >= n
        
