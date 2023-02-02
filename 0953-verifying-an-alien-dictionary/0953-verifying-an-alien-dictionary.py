class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hmap = {}
        for i in range(len(order)):
            hmap[order[i]] = i

        return words == sorted(words, key = lambda x: [hmap[i] for i in x])