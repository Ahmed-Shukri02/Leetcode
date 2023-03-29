class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:

        satisfaction = sorted(satisfaction)
        mem = {}

        def dfs(i, prev_dish):
            if i >= len(satisfaction):
                return 0
            
            if (i, prev_dish) not in mem:
                # include or excluse
                inc, exc = float("-inf"), float("-inf")
                if satisfaction[i] < 0:
                    exc = dfs(i + 1, prev_dish)
                inc = (satisfaction[i] * prev_dish) + dfs(i + 1, prev_dish + 1)

                mem[(i, prev_dish)] = max(inc, exc)

            return mem[(i, prev_dish)]

        return dfs(0, 1)