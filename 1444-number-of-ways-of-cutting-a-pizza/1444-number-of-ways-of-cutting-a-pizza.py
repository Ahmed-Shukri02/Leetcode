class Solution:
    def ways(self, pizza: List[str], k: int) -> int:

        mem = {} # {(top, left, n, m): k} -> describes max number of cuts described by (top, left) and (top + n - 1, left + m - 1).
        ROWS, COLS = len(pizza), len(pizza[0])

        def validate(top, left, n, m):
            return any(["A" in s[left:left+m] for s in pizza[top:top+n]])

        def dfs(top, left, n, m, k):
            if k == 0:
                return 1 if validate(top, left, n, m) else 0
            elif n == m == 1:
                return 0

            if (top, left, n, m, k) not in mem: 
                # choose to split vertically or horizontally
                f = 0
                for new_top in range(top + 1, ROWS):
                    if not validate(top, left, new_top - top, m):
                        continue
                    f += dfs(new_top, left, ROWS - new_top, m, k-1)

                for new_left in range(left + 1, COLS):
                    if not validate(top, left, n, new_left - left):
                        continue
                    f += dfs(top, new_left, n, COLS - new_left, k-1)
                
                mem[(top, left, n, m, k)] = f

            return mem[(top, left, n, m, k)]
        
        return dfs(0, 0, ROWS, COLS, k - 1) % ((10**9) + 7)