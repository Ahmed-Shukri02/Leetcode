class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        length = len(s)
        mem = [None] * length
        
        def dfs(i):
            if i >= length:
                return True
            if mem[i] != None:
                return mem[i]
            
            res = False
            for j in range(i, length):
                if s[i:j+1] in wordDict and dfs(j+1):
                    res = True
            mem[i] = res
            return res
        
        return dfs(0)