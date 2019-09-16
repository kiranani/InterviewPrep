class Solution:
    def nextClosestTime(self, time: str) -> str:
        l = sorted([int(x) for x in time if x != ":"])
        if len(l) == 1: return time
        t = int(time[:2]) * 60 + int(time[3:])
        times, s = [], set()
        for h1, h2, m1, m2 in itertools.product(l, repeat = 4):
            hh, mm = 10 * h1 + h2, 10 * m1 + m2
            if (hh, mm) not in s and hh < 24 and mm < 60:
                s.add((hh, mm))
                times.append(hh * 60 + mm)
        n = len(times)
        l, r, a = 0, n - 1, -1
        while l <= r:
            m = (l + r) // 2
            if times[m] == t:
                a = m + 1
                break
            elif times[m] > t:
                r = m - 1
            else:   
                l = m + 1
        if a == n: a = 0
        return "{:02d}:{:02d}".format(*divmod(times[a], 60))
        
                 
