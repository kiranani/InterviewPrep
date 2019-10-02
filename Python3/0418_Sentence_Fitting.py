class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        line = " ".join(sentence) + " "
        j, n = 0, len(line)
        for i in range(rows):
            j += cols
            if line[j % n] == " ":
                j += 1
            else:
                while line[(j - 1) % n] != " ":
                    j -= 1
        return j // n
        
        
