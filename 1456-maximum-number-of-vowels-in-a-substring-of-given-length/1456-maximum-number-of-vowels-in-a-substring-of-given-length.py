class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # sliding window approach
        vowels, f = set(["a", "e", "i", "o", "u"]), 0
        curr = 0
        l, r = 0, 0
        for i in range(k): # initialise sliding window
            if s[i] in vowels:
                curr += 1
            r += 1
            
        while r < len(s):
            f = max(f, curr)
            # add r, remove l
            if s[r] in vowels:
                curr += 1
            if s[l] in vowels:
                curr -= 1
            l, r = l + 1, r + 1

        f = max(f, curr)
        return f
        

