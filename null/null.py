class TrieNode:
    def __init__(self):
        self.children = {}
        self.terminal = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        tmp = self.root
        for char in word:
            if char not in tmp.children:
                tmp.children[char] = TrieNode()
            tmp = tmp.children[char]
        tmp.terminal = True

    def search(self, word: str) -> bool:
        tmp = self.root
        for char in word:
            if char not in tmp.children:
                return False
            tmp = tmp.children[char]
        return tmp.terminal

    def startsWith(self, prefix: str) -> bool:
        tmp = self.root
        for char in prefix:
            if char not in tmp.children:
                return False
            tmp = tmp.children[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)