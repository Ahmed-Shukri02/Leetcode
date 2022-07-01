class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # Complexities:
        # Time: O(nmlogm)
        # Space: O(n)   
        
        hmap1 = {}
        
        # sort every element
        for i in range(len(strs)): # O(n)
            sort = "".join(sorted(strs[i])) # O(2mlogm)
            
            if not hmap1.get(sort):
                hmap1[sort] = [strs[i]]
            else:
                hmap1[sort].append(strs[i])
        
        return hmap1.values()