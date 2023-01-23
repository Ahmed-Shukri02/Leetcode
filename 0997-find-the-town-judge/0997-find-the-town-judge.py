class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted, trusting = defaultdict(int), defaultdict(int)
        for s, d in trust:
            trusted[d] += 1
            trusting[s] += 1
        for i in range(1, n + 1):
            if not trusting[i] and trusted[i] == n - 1:
                return i
        return -1 