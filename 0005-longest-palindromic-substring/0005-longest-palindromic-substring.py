class Solution:
    def longestPalindrome(self, s: str) -> str:
        final = 0
        string = ""
        length = len(s)
        for i in range(length):
            l, r = i, i
            if s[l] == s[r]:
                curr = 1
                while l >= 0 and r < length and s[l] == s[r]:
                    curr += 2
                    l, r = l - 1, r + 1
                if curr > final:  
                    final = curr
                    string = s[l + 1: r]
            
            l, r = i, i + 1
            if l >= 0 and r < length and s[l] == s[r]:
                curr = 2
                while l >= 0 and r < length and s[l] == s[r]:
                    curr += 2
                    l, r = l - 1, r + 1
                if curr > final:  
                    final = curr
                    string = s[l + 1: r]
        
        return string