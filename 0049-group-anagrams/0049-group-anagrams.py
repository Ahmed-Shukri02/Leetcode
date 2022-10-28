class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        length = len(strs)
        hmap = {}
        for s in strs:
            set1 = "".join(sorted(s))
            
            if set1 in hmap:
                hmap[set1].append(s)
            else:
                hmap[set1] = [s]
        
        return list(hmap.values())
        
        