class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        banned = set(banned)
        import re
        words = re.split("\W", paragraph)
        counts = collections.defaultdict(int)
        for word in words:
            word = word.lower()
            if word != "" and word not in banned:
                counts[word] += 1
        return max(counts.items(), key=lambda x: x[1])[0]
        
