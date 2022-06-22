class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        # start by making a dictionary of letter/occurances for both
        ransomDict, magDict = {}, {}
        # let n be length of ransom note and m be of magazine
        # let p and q also be the number of distinct letters in ransomNote and magazine respectively
        # Total complexity for algorithm:
        # Time: O(nm)
        # Space: O(pq)
        
        
        # ransom letter dict complexity: time = O(n), space = O(p) where p is the number of distinct letters in ransomNote
        for letter in ransomNote:
            ransomDict[letter] = 1 + ransomDict.get(letter, 0)
        # magazine dict complexity: time = O(m), space = O(q) where q is the number of distinct letters in magazine
        for letter in magazine:
            magDict[letter] = 1 + magDict.get(letter, 0)
        
        # for each key in ransomDict, see if there is enough or more of that letter in magazine.
        # complexities: time = O(p), space = O(1)
        for key in ransomDict:
            if ransomDict[key] > magDict.get(key, 0): 
                return False
        
        return True
    