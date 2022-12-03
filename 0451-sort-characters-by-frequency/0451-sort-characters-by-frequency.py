class Solution:
    def frequencySort(self, s: str) -> str:
        hmap = {}
        for char in s:
            hmap[char] = hmap.get(char, 0) + 1
        final = sorted([i for i in hmap.keys()], key = lambda x: -hmap[x])
        
        f = ""
        for char in final:
            f += char * hmap[char]
        return f