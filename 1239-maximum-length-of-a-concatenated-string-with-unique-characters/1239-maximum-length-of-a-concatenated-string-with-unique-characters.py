class Solution:
    def maxLength(self, arr: List[str]) -> int:
        final = [0]
        def dfs(hset, i):
            if i >= len(arr):
                final[0] = max(final[0], len(hset))
                return

            # decision: include itself or not
            # bf: check if chars in hset
            dfs(hset.copy(), i + 1)

            for char in arr[i]:
                if char in hset:
                    return
                hset.add(char)

            dfs(hset.copy(), i + 1)


        dfs(set(), 0)
        return final[0]