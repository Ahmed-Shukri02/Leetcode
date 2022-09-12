class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        
        
        final = []
        
        
        def is_palindrome(l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        def palindrome(i, curr):
            if i >= len(s): # exceeded limit
                final.append([i for i in curr])
                return

            for j in range(i, len(s)):
                if is_palindrome(i, j):
                    curr.append(s[i:j+1])
                    palindrome(j+1, curr)
                    curr.pop()
            
        palindrome(0, [])
        return final