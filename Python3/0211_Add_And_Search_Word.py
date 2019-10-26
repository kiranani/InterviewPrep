class Trie:
    def __init__(self):
        self.ending = False
        self.children = {}
        
    def search(self, word):
        if not word or not self.children:
            return False
        if len(word) == 1:
            if word == ".":
                return any(child.ending for child in self.children.values())
            else:
                return self.children.get(word) and self.children[word].ending
        else:
            c = word[0]
            word = word[1:]
            if c == ".":                
                for child in self.children.values():
                    if child.search(word):
                        return True
            elif c in self.children:
                return self.children[c].search(word)
            else:
                return False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        t = self.trie
        for c in word:
            if c not in t.children:
                t.children[c] = Trie()
            t = t.children[c]
        t.ending = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.trie.search(word)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
