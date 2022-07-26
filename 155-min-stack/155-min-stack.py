class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        
        self.stack.append(val)
        if self.minStack:
            if val <= self.minStack[-1]:
                self.minStack.append(val)
        else:
            self.minStack.append(val)
        
        
    def pop(self):
        """
        :rtype: None
        """
        
        if self.stack[-1] == self.minStack[-1]:
            # we are removing the minimum value, return minimum stack to previous minVal
            self.minStack.pop()
            print(self.minStack)
        
        # remove from stack
        self.stack.pop()  

    def top(self):
        """
        :rtype: int
        """
        # grab last value of stack
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()