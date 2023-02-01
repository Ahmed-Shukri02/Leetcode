class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        a1, a2 = set([]), set([])
        for i in range(len(str1)):
            l = i + 1
            if len(str1) % l != 0: continue
            mul = len(str1) // l
            if str1[:i + 1] * mul == str1:
                a1.add(str1[:i + 1])

        for i in range(len(str2)):
            l = i + 1
            if len(str2) % l != 0: continue
            mul = len(str2) // l
            if str2[:i + 1] * mul == str2:
                a2.add(str2[:i + 1])
        
        # intersection of dictionaries
        ans = a1.intersection(a2)
        return max(ans) if ans else ""
        


        

        

