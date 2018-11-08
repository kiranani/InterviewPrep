class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if not timeSeries or not duration:
            return 0
        start, end, total = timeSeries[0], timeSeries[0] + duration, 0
        for time in timeSeries[1:]:
            if time < end:
                end = time + duration
            else:
                total += end - start
                start, end = time, time + duration
        total += end - start
        return total
        
