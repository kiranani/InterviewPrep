class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = []
        h = collections.Counter(s)
        for c in sorted(h.items(), key=operator.itemgetter(1), reverse=True):
            l.extend([c[0]] * c[1])
        return "".join(l)
   
