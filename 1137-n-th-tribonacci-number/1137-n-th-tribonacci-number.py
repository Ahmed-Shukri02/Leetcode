class Solution:
    def tribonacci(self, n: int) -> int:
        n1, n2, n3 = 0, 1, 1
        if n == 0:
            return n1
        elif n in (1, 2):
            return n3

        for i in range(3, n + 1):
            new = n1 + n2 + n3
            n1 = n2
            n2 = n3
            n3 = new
        return n3
