class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        num_stack = []
        
        for i in range(len(tokens)):
            if tokens[i] not in ("+", "-", "/", "*"):
                tokens[i] = int(tokens[i])
        
        for char in tokens:
            if char == "+":
                num_stack.append(num_stack.pop() + num_stack.pop())
            elif char == "-":
                a, b = num_stack.pop(), num_stack.pop()
                num_stack.append(b - a)
            elif char == "*":
                num_stack.append(num_stack.pop() * num_stack.pop())
            elif char == "/":
                a, b = num_stack.pop(), num_stack.pop()
                num_stack.append(int(float(b)/a))
            else:
                num_stack.append(int(char))
        
        print(num_stack[0])
        return num_stack[0]