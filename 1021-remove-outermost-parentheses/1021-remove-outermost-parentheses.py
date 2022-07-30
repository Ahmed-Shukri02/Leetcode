class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        final = ""
        
        # create stack
        for char in s:
            if char == ")":
                stack.pop()
                # add to final if stack is not empty
                if stack:
                    final += char
                
            elif char == "(":
                # add to final if stack is not empty
                if stack:
                    final += char
                
                stack.append( "(")
        
        return final