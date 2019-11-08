class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        s = [envelopes[0][1]]
        def bs(t):
            l, r = 0, len(s)
            while l <= r:
                m = (l + r) >> 1
                if s[m] == t:
                    return m
                elif s[m] < t:
                    l = m + 1
                else:
                    r = m - 1
            return l
        for env in envelopes[1:]:
            if env[1] > s[-1]:
                s.append(env[1])
            else:
                s[bs(env[1])] = env[1]
        return len(s)
            
        
        
