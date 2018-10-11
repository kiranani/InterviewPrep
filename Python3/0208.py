class Node:
    def __init__(self, char, isEnding):
        self.char = char
        self.children = {}
        self.isEnding = isEnding
        
        
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node(None, False)
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        n, d = len(word), self.root.children
        for i, c in enumerate(word):
            if d.get(c) is None:
                d[c] = Node(c, i == n - 1)
            elif i == n - 1:
                d[c].isEnding = True
            d = d[c].children
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        d = self.root
        for c in word:
            if d.children.get(c) is None:
                return False
            d = d.children[c]
        return d.isEnding
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        d = self.root.children
        for c in prefix:
            if d.get(c) is None:
                return False
            d = d[c].children
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
