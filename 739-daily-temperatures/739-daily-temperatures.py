class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
        length = len(temperatures)
        final = [0] * length
        stack= []
        
        l = 0
        while l < length:
            # if stack is empty
            if not stack:
                stack.append((temperatures[l] , l))
                l += 1
                continue
            # if value is larger than top of stack
            while stack and temperatures[l] > stack[-1][0]:
                final[stack[-1][1]] = l - stack[-1][1]
                stack.pop()
            
            #append value to stack and continue
            stack.append((temperatures[l], l))
            l += 1
        return final