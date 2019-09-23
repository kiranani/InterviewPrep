class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        i = 1
        while reader.get(i) < target:
            i <<= 1
        l, r = i >> 1, i
        while l <= r:
            m = (l + r) // 2
            am = reader.get(m)
            if am == target:
                return m
            elif am > target:
                r = m - 1
            else:
                l = m + 1
        return -1
        
        
