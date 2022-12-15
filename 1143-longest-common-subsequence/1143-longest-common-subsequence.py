class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1, l2 = len(text1), len(text2)
        mem ={}
        def dfs(i, j):
            if i >= l1 or j >= l2:
                return 0
            
            if (i, j) not in mem:
                inci, incj = float("-inf"), float("-inf")
                incb = dfs(i+1, j+1)
                if text1[i] == text2[j]:
                    incb += 1
                else:
                    inci, incj = dfs(i + 1, j), dfs(i, j+1)
                mem[(i, j)] = max(inci, incj, incb)
            
            return mem[(i, j)]
        
        return dfs(0, 0)