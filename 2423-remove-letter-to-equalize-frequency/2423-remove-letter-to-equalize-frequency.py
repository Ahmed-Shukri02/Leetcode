class Solution:
    def equalFrequency(self, word: str) -> bool:
        def isPossible(word):
            hmap = defaultdict(int)
            for char in word:
                hmap[char] += 1
            return len(set(hmap.values())) == 1
        
        for i in range(len(word)):
            if isPossible(word[:i] + word[i + 1:]): return True
        return False


        
        