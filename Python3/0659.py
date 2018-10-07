class Solution:
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def emptySubs(s):
            for sub in s:
                if sub < 3:
                    return False
            s[:] = []
            return True

        def updateSubs(s, c):
            #print(s, c)
            if c < 0:
                for i in range(c, 0):
                    if s[0] < 3:
                        return False
                    else:
                        s[:] = s[1:]
                s[:] = [x + 1 for x in s]
            elif c > 0:
                s[:] = [x + 1 for x in s]
                s.extend([1] * c)
            else:
                s[:] = [x + 1 for x in s]
            return True

        pairs, n, i, s, prev, prevCount = [], len(nums), 0, [], None, 0
        if n < 3:
            return False
        while i < n:
            num, count, i = nums[i], 1, i + 1
            while i < n and nums[i] == num:
                count += 1
                i += 1
            if prev is not None:
                if num - prev > 1:
                    isValid = emptySubs(s)
                    if not isValid:
                        return False
                    updateSubs(s, count)
                else:
                    if count == prevCount:
                        updateSubs(s, 0)
                    else:
                        isValid = updateSubs(s, count - prevCount)
                        if not isValid:
                            return False
            else:
                updateSubs(s, count)
            #print(num, count, s)
            prev, prevCount = num, count           
            pairs.append((num, count))

        return emptySubs(s)
