class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:

        mem = {}
        def compare(w1, w2):
            h1, h2 = defaultdict(int), defaultdict(int)
            for char in w1:
                h1[char] += 1
            for char in w2:
                h2[char] += 1
            return h1 == h2

        def dfs(w1, w2):
            if len(w1) != len(w2) or not compare(w1, w2):
                mem[(w1, w2)] = False
                return False
            elif len(w1) == 1:
                return True
            
            if (w1, w2) not in mem:
                f = False
                for i in range(1, len(w1)):
                    f = f or (dfs(w1[:i], w2[:i]) and dfs(w1[i:], w2[i:])) or (dfs(w1[:i], w2[-i:]) and dfs(w1[i:], w2[:-i]))
                mem[(w1, w2)] = f
            
            return mem[(w1, w2)]

        return dfs(s1, s2)
            
