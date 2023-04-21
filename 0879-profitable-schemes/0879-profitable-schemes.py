class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:

        mem = {}
        arr = [(group[i], profit[i]) for i in range(len(group))]
        arr = sorted(arr, key = lambda x: x[0])

        def dfs(i, k, prof):
            if i >= len(arr) or k < arr[i][0]:
                return 1 if prof >= minProfit else 0
            if (i, k, min(minProfit, prof)) not in mem:
                f = 0
                if arr[i][0] <= k:
                    # choose to do the crime or not
                    f += dfs(i + 1, k - arr[i][0], prof + arr[i][1]) + dfs(i + 1, k, prof)
                mem[(i, k, min(minProfit, prof))] = f

            return mem[(i, k, min(minProfit, prof))]

        return dfs(0, n, 0) % ((10 **9) + 7)
