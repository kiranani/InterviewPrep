class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        citations.sort()
        n, j = len(citations), len(citations) - 1
        while j > -1:
            if citations[j] < (n - j):
                return n - j - 1
            j -= 1
        return n
