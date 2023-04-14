class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        mem = {}
        def dfs(l, r):
            if l == r:
                return 1
            elif l > r:
                return 0

            if (l, r) not in mem:
                if s[l] == s[r]:
                    mem[(l, r)] = 2 + dfs(l + 1, r - 1)
                else:
                    mem[(l, r)] = max(dfs(l + 1, r), dfs(l, r - 1))

            return mem[(l, r)] 
        return dfs(0, len(s) - 1)