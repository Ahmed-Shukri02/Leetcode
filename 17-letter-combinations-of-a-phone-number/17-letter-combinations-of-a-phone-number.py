class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        if not digits:
            return []
        
        final = []
        hmap = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        
        def combination(index, curr):
            if index >= len(digits):
                final.append("".join(curr))
                return
            # for current index, run recursively with all possible character
            for char in hmap[digits[index]]:
                curr.append(char)
                combination(index + 1, curr)
                curr.pop()
        combination(0, [])
        return final
            