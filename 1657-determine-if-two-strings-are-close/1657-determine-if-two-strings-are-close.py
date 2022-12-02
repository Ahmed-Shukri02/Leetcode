class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        h1, h2 = {}, {}
        
        # if lengths of words are not equal, no transforming or swapping will get the same string
        l1, l2 = len(word1), len(word2)
        if l1 != l2:
            return False
        
        # count every character in word1: O(n) / O(n)
        for char in word1:
            h1[char] = h1.get(char, 0) + 1
        
        # count every character in word2, and return false if it doesn't appear in word1: O(n) / O(n)
        for char in word2:
            if char not in h1:
                return False
            h2[char] = h2.get(char, 0) + 1
        
        # check the other way around, and check character equality
        equal = True
        for char in h1.keys():
            if char not in h2:
                return False
            if h2[char] != h1[char]:
                equal = False
        if equal: return True # simply doing swapping operations will get you there.
        
        # occurances of each character not the same, now check if occurances of occurances is the same
        o1, o2 = {}, {}
        for occurances in h1.values():
            o1[occurances] = o1.get(occurances, 0) + 1
        for occurances in h2.values():
            o2[occurances] = o2.get(occurances, 0) + 1
        
        # return if the two are equal
        return o1 == o2