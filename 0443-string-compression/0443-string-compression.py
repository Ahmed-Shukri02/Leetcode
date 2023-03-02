class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        c = 0
        
        if len(chars) == 1:
            return 1

        prev = chars[0]
        for char in chars:
            if char == prev:
                c += 1
            else:
                s += prev 
                if c > 1: s += str(c)
                c = 1
                prev = char
        s += prev 
        if c > 1: s += str(c)

        for i in range(len(s)):
            chars[i] = s[i]
            
        return len(s)