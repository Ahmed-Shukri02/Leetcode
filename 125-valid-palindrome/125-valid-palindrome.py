class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # O(n) time with O(n) space
        
        s = s.lower()
        l, r = 0, len(s) - 1
        while r > l:
            if not s[r].isalnum():
                r -= 1
                continue
            if not s[l].isalnum():
                l += 1
                continue
            
            if s[l] != s[r]:
                return False
            r -= 1
            l += 1
        return True