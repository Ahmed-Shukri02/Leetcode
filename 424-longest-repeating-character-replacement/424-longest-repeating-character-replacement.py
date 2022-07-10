class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # Complexities:
        # Time: O(n)
        # Space: O(n)
        
        
        l, r = 0, 1
        windowLen, maxWindowLen = 1, 1
        maxCount = 0
        length = len(s)
        hmap = {s[l]: 1}
        while r < length:
            hmap[s[r]] = hmap.get(s[r], 0) + 1
            maxCount = max(hmap.values())
            windowLen += 1
            
            while (windowLen - maxCount) > k:
                hmap[s[l]] -= 1
                windowLen -= 1
                l += 1
                maxCount = max(hmap.values())
            
            maxWindowLen = max(maxWindowLen, windowLen)
            r += 1
            
        return max(maxWindowLen, windowLen)