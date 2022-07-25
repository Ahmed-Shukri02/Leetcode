class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # initialise stack
        stack = []
        
        # have closing hmap:
        hmap = {"]" : "[", "}" : "{", ")": "("}
        
        for char in s:
            if char in hmap:
                # check if opening tag is at the top of the stack
                if len(stack) != 0 and stack[-1] == hmap[char]:
                    stack.pop()
                else: return False
            else:
                stack.append(char)
        
        
        return len(stack) == 0