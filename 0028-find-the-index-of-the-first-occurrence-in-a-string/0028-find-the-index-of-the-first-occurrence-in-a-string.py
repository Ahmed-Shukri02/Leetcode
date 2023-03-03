class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == haystack:
            return 0

        pre = needle[0]
        trial = []
        for i in range(len(haystack)):
            if haystack[i] == pre:
                trial.append(i)

        def validate(i):
            p1, p2 = i, 0
            while p1 < len(haystack) and p2 < len(needle) and haystack[p1] == needle[p2]:
                p1, p2 = p1 + 1, p2 + 1
            if p2 == len(needle):
                return True

        for t in trial:
            if validate(t): return t
        return -1

