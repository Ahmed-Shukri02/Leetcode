class Solution:
    def countOdds(self, low: int, high: int) -> int:
        f = ((high - low) // 2) + 1
        if low % 2 == 0 and high % 2 == 0: f -= 1
        return f