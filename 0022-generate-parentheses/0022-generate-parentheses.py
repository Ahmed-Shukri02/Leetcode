class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        stack, result= [], []
        
        def Recursive(openN, closeN):
            if openN == closeN == n:
                # reached the end
                result.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                Recursive(openN + 1, closeN)
                stack.pop()
            
            if closeN < openN:
                stack.append(")")
                Recursive(openN, closeN + 1)
                stack.pop()
        
        Recursive(0, 0)
        return result