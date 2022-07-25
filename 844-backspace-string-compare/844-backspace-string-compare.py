class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_stack, t_stack = [], []
        
        # go through s
        for char in s:
            if char == "#":
                if len(s_stack) != 0:
                    s_stack.pop()
            else:
                s_stack.append(char)
        
        for char in t:
            if char == "#":
                if len(t_stack) != 0:
                    t_stack.pop()
            else:
                t_stack.append(char)
        
        return s_stack == t_stack