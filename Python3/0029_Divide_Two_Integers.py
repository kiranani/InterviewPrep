class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        neg = (dividend < 0) ^ (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        def findDiv(dvd, dvs):
            c = 1
            while dvd >= (dvs << 1):
                dvs <<= 1
                c <<= 1
            return c, dvd - dvs
        cnt = 0
        while dividend >= divisor:
            c, dividend = findDiv(dividend, divisor)
            cnt += c
        if cnt > (1 << 31) - 1 and not neg:
            return (1 << 31) - 1
        return -cnt if neg else cnt
        
        
