class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:

        flipMap = {"1": "0", "0": "1"}
        mem = {}
        def dfs(i, prev):
            if i >= len(s):
                return 0  
            flip, cont = float("inf"), float("inf")
            if (i, prev) not in mem:
                if prev == "0":
                    cont = dfs(i + 1, s[i])
                    flip = 1 + dfs(i + 1, flipMap[s[i]])
                elif s[i] == "0":
                    # previous is a 1 digit, this digit must be flipped
                    flip = 1 + dfs(i + 1, "1")
                else:
                    cont = dfs(i + 1, s[i])
                mem[(i, prev)] = min(flip, cont)
            return mem[(i, prev)]
        
        return dfs(0, "0")