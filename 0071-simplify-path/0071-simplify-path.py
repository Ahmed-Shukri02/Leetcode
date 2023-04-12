class Solution:
    def simplifyPath(self, path: str) -> str:
        # if top of stack is dot, then remove two from stack
        # if top of stack is not dot, add

        s = []
        for p in path.split("/"):
            if p == "..":
                if s: s.pop()
            elif p and p != ".":
                s.append(p)

        return "/" + "/".join(s)