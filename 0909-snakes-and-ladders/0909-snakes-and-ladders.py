class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        arr = []
        for i in range(len(board)):
            if (len(board) - i) % 2 == 1:
                arr += reversed(board[i])
            else:
                arr += board[i]
        arr = list(reversed(arr))

        n = len(arr)
        q = deque([0])
        ans = [-1] * n
        ans[0] = 0
        while q:
            val = q.popleft()
            for j in range(val + 1, min(val + 7, n)):
                pos = j if arr[j] == -1 else arr[j] - 1
                if ans[pos] == -1:
                    ans[pos] = ans[val] + 1
                    q.append(pos)

        return ans[n - 1]