class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True
        capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if word[0] in capital and word[1] in capital:
            for i in range(1, len(word)):
                if word[i] not in capital:
                    return False
        else:
            for i in range(1, len(word)):
                if word[i] in capital:
                    return False
        return True
