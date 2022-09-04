class TrieNode:
    def __init__(self, terminate = False):
        self.children = {}
        self.terminate = terminate

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        
        tmp = self.root
        for letter in word:
            if letter in tmp.children:
                tmp = tmp.children[letter]
                continue
            else:
                tmp.children[letter] = TrieNode()
                tmp = tmp.children[letter]
        # at end of word
        tmp.terminate = True
        
        print(tmp.children)

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        tmp = self.root
        for letter in word:
            if letter not in tmp.children:
                print(letter)
                return False
            else:
                tmp = tmp.children[letter]
        if not tmp.terminate:
            return False
        else:
            return True
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        tmp = self.root
        for letter in prefix:
            if letter not in tmp.children:
                print(letter)
                return False
            else:
                tmp = tmp.children[letter]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)