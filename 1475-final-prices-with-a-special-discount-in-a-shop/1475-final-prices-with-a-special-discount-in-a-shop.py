class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        stack = []
        length = len(prices)
        final = [i for i in prices]
        
        # we consider the first value of the stack added
        l = 0
        while l < length:
            if not stack:
                stack.append((prices[l], l))
                l += 1
                continue
            
            # check if current value is larger than stack values
            while stack and stack[-1][0] >= prices[l]:
                final[stack[-1][1]] = stack[-1][0] - prices[l]
                stack.pop()
                
            # append current value
            stack.append((prices[l], l))
            l += 1
            
        return final