class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Complexities:
        # Time: O(n)
        # Space: O(n)
        
        maxLength = 0
        length = len(s)
        
        # edge cases
        if length == 0:
            return 0
        elif length == 1:
            return 1
        
        l, r = 0, 1
        counter = 1
        values = set(s[l])
        while r < length:
            if s[r] in values:
                maxLength = max(counter, maxLength)
                while l < r:
                    if s[l] != s[r]:
                        values.remove(s[l])
                        print("removed" + s[r])
                        l += 1
                        counter -= 1
                    else:
                        l += 1
                        break
                r += 1
                    
            else:
                values.add(s[r])
                print("added" + s[r])
                counter += 1
                r += 1
        
        maxLength = max(counter, maxLength)
        return maxLength