class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        length = len(s)
        mem = {length: 1}
        
        def dfs(i):
            if i in mem:
                return mem[i]
            if s[i] == "0":
                return 0
            
            perms = 0
            # single digit
            perms += dfs(i + 1)
            
            #double digit
            if i + 1 < length and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456" )):
                perms += dfs(i + 2)
            
            mem[i] = perms
            return perms
        
        return dfs(0)