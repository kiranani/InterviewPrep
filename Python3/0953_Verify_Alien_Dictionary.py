class Solution:
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        alphas = {x: i for i, x in enumerate(order)}
        def compare(w1, w2):
            n1, n2 = len(w1), len(w2)
            i = 0
            while i < n1 and i < n2:
                if alphas[w1[i]] < alphas[w2[i]]:
                    return -1
                elif alphas[w1[i]] > alphas[w2[i]]:
                    return 1
                else:
                    i += 1
            if i == n1 and i == n2:
                return 0
            elif i == n2:
                return 1
            else:
                return -1
        for i in range(len(words) - 1):
            if compare(words[i], words[i + 1]) > 0:
                return False
        return True
        
