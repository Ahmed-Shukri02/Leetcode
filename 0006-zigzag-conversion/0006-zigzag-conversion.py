class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        l = len(s)
        hmap = defaultdict(str)
        i, curr = 0, 0
        while i < l:
            if curr >= numRows:
                curr -= 1
                while i < l and curr > 0:
                    curr -= 1
                    hmap[curr] += s[i]
                    i += 1
                curr += 1
                continue
            hmap[curr] += s[i]
            i, curr = i + 1, curr + 1
        
        f = ""
        for j in sorted(hmap.keys()):
            f += hmap[j]
        return f


