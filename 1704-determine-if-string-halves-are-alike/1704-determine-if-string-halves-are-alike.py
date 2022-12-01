class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set(["a", "e", "i", "o", "u"])
        length = len(s)
        l, r = 0, int(length / 2)
        v1, v2 = 0, 0
        for i in range(int(length /2)):
            if s[l].lower() in vowels:
                v1 += 1    
            if s[r].lower() in vowels:
                v2 += 1
            l,r = l + 1, r + 1
        
        return v1 == v2
        
            