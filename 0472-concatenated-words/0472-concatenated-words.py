class TrieNode:
    def __init__(self):
        self.children = {}
        self.terminal = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.mem = {}

    def add(self, word):
        tmp = self.root
        for char in word:
            if char not in tmp.children:
                tmp.children[char] = TrieNode()
            tmp = tmp.children[char]
        tmp.terminal = True

    def searchTree(self, word):
        # DP (NOT IMPLEMENTED LOL)
        if not word:
            return 0
        tmp = self.root
        m = float("-inf")
        for i in range(len(word)):
            if word[i] not in tmp.children:
                break
            elif tmp.children[word[i]].terminal:
                m = max(m, 1 + self.searchTree(word[i+1:]))
            tmp = tmp.children[word[i]]
        return m


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words = sorted(words, key = lambda x: len(x))
        myTrie = Trie()
        final = []
        for word in words:
            concat = myTrie.searchTree(word)
            if concat != float("-inf") and concat >= 2:
                final.append(word)
            myTrie.add(word)
        return final

