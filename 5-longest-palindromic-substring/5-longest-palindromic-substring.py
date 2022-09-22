class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        final = ""
        flen = 0
        length = len(s)
        for i in range(length):
            # consider each elem to be center of palindrome
            l, r = i, i
            while l >= 0 and r < length and s[l] == s[r]:
                if (r - l + 1) > flen:
                    final = s[l: r+1]
                    flen = r - l + 1
                l -= 1
                r += 1
            
            l, r = i, i + 1
            while l >= 0 and r < length and s[l] == s[r]:
                if (r - l + 1) > flen:
                    final = s[l: r+1]
                    flen = r - l + 1
                l -= 1
                r += 1
        
        return final