class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        q = deque([i for i in senate])
        d, r = 0, 0
        while q:
            l = len(q)
            for i in range(l):
                n = q.popleft()
                if (n == "R" and not r) or (n == "D" and not d):
                    q.append(n)
                    if n == "R":
                        d += 1
                    else:
                        r += 1
                elif n == "R":
                    r -= 1
                elif n == "D":
                    d -= 1
            if len(set(q)) == 1:
                break
        return "Radiant" if q[0] == "R" else "Dire"
            


