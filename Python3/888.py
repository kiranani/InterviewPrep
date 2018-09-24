class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        a, b = set(), set()
        sumA, sumB = 0, 0
        for x in A:
            a.add(x)
            sumA += x
        for y in B:
            b.add(y)
            sumB += y
        diff = abs((sumA - sumB) // 2)
        boo = False
        if sumA > sumB:
            a, b = b, a
            boo = True
        for x in a:
            if x + diff in b:
                return [x + diff, x] if boo else [x, x + diff]
