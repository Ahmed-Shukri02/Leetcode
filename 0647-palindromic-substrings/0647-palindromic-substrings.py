class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # O(n^2)
        
        final = 0
        length = len(s)
        for i in range(len(s)):
            # treat each char as center of palindrome
            l, r = i, i
            while l >= 0 and r < length:
                if s[l] != s[r]:
                    break
                final += 1
                l -= 1
                r += 1
            
            # for even palindromes
            l, r = i, i + 1
            while l >= 0 and r < length:
                if s[l] != s[r]:
                    break
                final += 1
                l -= 1
                r += 1
        return final