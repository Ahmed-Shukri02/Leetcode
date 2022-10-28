class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        length = len(strs)
        hmap = {}
        for s in strs:
            set1 = [0 for i in range(26)]
            for char in s:
                set1[ord(char) - 97] = set1[ord(char) - 97] + 1
            
            t = tuple(set1)
            if t in hmap:
                hmap[t].append(s)
            else:
                hmap[t] = [s]
        
        return list(hmap.values())
        
        