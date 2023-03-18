class BrowserHistory:

    def __init__(self, homepage: str):
        self.s = [homepage]
        self.bl = []

    def visit(self, url: str) -> None:
        self.s.append(url)
        self.bl = []

    def back(self, steps: int) -> str:
        while steps > 0 and len(self.s) > 1:
            self.bl.append(self.s.pop())
            steps -= 1
        return self.s[-1]

    def forward(self, steps: int) -> str:
        while steps > 0 and self.bl:
            self.s.append(self.bl.pop())
            steps -= 1
        return self.s[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)