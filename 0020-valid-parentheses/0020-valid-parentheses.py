class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        op = {")": "(", "}": "{", "]": "["}
        
        stack = []
        for char in s:
            if char in (")", "]", "}"):
                if not stack or stack[-1] != op[char]:
                    return False
                else: stack.pop()
            else:
                stack.append(char)
                
        return not stack