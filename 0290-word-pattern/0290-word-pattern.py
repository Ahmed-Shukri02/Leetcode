class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        h1, h2 = {}, {}
        words = s.split(" ")
        l1, l2 = len(words), len(pattern)
        if l1 != l2:
            return False
        for i in range(l1):
            if not h1.get(pattern[i], None) and not h2.get(words[i], None):
                h1[pattern[i]], h2[words[i]] = words[i], pattern[i]
            elif h1.get(pattern[i], None) != words[i] or h2.get(words[i], None) != pattern[i]:
                return False
        return True