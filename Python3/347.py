class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        h = {}
        for num in nums:
            h[num] = h.setdefault(num, 0) + 1
        h = sorted(h.items(), key=operator.itemgetter(1, 0), reverse=True)
        return [x[0] for x in h[:k]]
    
