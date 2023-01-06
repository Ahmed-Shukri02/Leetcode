class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs = sorted(costs)
        f, i = 0, 0
        l = len(costs)
        while i < l and costs[i] <= coins:
            coins -= costs[i]
            f += 1
            i += 1
        return f
        