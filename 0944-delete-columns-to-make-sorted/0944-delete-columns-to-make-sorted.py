class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        final = 0
        for j in range(len(strs[0])):
            i = 0
            while i + 1 < n:
                if ord(strs[i][j]) > ord(strs[i+1][j]):
                    final += 1
                    break
                i += 1
        return final
                

