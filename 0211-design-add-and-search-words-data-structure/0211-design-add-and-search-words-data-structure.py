class TrieNode:
    def __init__(self):
        self.children = {}
        self.terminal = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()


    def addWord(self, word: str) -> None:
        tmp = self.root
        for char in word:
            if char not in tmp.children:
                tmp.children[char] = TrieNode()
            tmp = tmp.children[char]
        tmp.terminal = True

    def search(self, word: str) -> bool:

        def dfs(tmp, i):
            if i >= len(word):
                return tmp.terminal
            t = False
            if word[i] == ".":
                for child in tmp.children.values():
                    t = t or dfs(child, i + 1)
            elif word[i] in tmp.children:
                t = dfs(tmp.children[word[i]], i + 1)
            return t

        return dfs(self.root, 0)




# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)