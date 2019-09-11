class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.char = ""
        self.d = {}
        self.end = False
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        c, n = word[0], len(word)
        node = self.d.get(c)
        if not node:
            self.d[c] = Trie()
            self.d[c].char = c
            node = self.d[c]
        if n == 1:
            node.end = True
        else:
            node.insert(word[1:])
            

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self
        for c in word:
            node = node.d.get(c)
            if not node:
                return False
        return node.end
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self
        for c in prefix:
            node = node.d.get(c)
            if not node:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)