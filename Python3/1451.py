from collections import defaultdict
class Solution:
    def arrangeWords(self, text: str) -> str:
        if text:
            words = text.split()
            d = defaultdict(list)
            for word in words:
                d[len(word)].append(word)
            words = [word.lower() for i in sorted(d) for word in d[i]]
            words[0] = words[0][0].upper() + words[0][1:]
            return " ".join(words)
        return ""
        
