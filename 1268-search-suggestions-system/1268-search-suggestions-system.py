class TrieNode:
    def __init__(self):
        self.children = {}
        self.terminate = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word):
        tmp = self.root
        for char in word:
            if char not in tmp.children:
                tmp.children[char] = TrieNode()
            tmp = tmp.children[char]
        tmp.terminate = True
    
    def suggest(self, prefix):
        # return a list of matches
        final = []
        tmp = self.root
        for char in prefix:
            if char not in tmp.children:
                return
            else:
                tmp = tmp.children[char]
        
        # recursively find every word spanning out of tmp node
        
        def suggestRecursive(node, word):
            if node.terminate:
                final.append(word)
            
            if not node.children: # leaf
                return
            
            for (letter, child) in node.children.items():
                suggestRecursive(child, word + letter)
        
        suggestRecursive(tmp, prefix)
        print(final)
        return sorted(final)[:3]
        
                

class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        trie = Trie()
        length = len(searchWord)
        
        for product in products:
            trie.add(product)
        
        final = []
        prefix = ""
        for i in range(length):
            prefix += searchWord[i]
            final.append(trie.suggest(prefix))
        return final