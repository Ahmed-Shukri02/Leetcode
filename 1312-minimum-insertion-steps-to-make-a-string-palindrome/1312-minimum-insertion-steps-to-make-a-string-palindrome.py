class Solution:
    def minInsertions(self, s: str) -> int:
        mem = {}
        def dfs(l, r):
            if l >= r:
                return 0

            if (l, r) not in mem:
                # check if palindrome
                if s[l] != s[r]:
                    # add left or right
                    mem[(l, r)] = 1 + min(dfs(l, r - 1), dfs(l + 1, r))
                else:
                    mem[(l, r)] = dfs(l + 1, r - 1)
            
            return mem[(l, r)]

        return dfs(0, len(s) - 1)
