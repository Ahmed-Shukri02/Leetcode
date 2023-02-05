class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        

        f = []
        if len(p) == 1:
            for i in range(len(s)):
                if s[i] == p: f.append(i)
            return f
        elif len(p) > len(s):
            return []

        
        def ind(char):
            return ord(char) - ord("a")
        
        chars = [0] * 26
        temp = [0] * 26
        for char in p:
            temp[ind(char)] += 1

        
        # set up window of length p
        l, r = 0, len(p) - 1
        for char in s[l:r]:
            chars[ind(char)] += 1

        while r < len(s):
            chars[ind(s[r])] += 1
            # validate
            if chars == temp:
                f.append(l)
            
            # move l and r
            chars[ind(s[l])] -= 1
            l += 1
            r += 1

        return f
        
        