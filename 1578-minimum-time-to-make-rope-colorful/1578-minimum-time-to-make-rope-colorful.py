class Solution(object):
    def minCost(self, colors, neededTime):
        """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
        """
        
        # greedy: time, space = O(n)

        length = len(colors)
        if length <= 1:
            return 0

        mem = [None] * length
        mem[-1] = 0
        stack = [length - 1] # use stack to keep track considering missing balloons
        for i in range(length - 2, -1, -1):
            if stack and colors[i] == colors[stack[-1]]: # if balloon is same color as the next balloon
                if neededTime[i] > neededTime[stack[-1]]: # if it takes shorter to remove next balloon than this one
                    ans = neededTime[stack.pop()]
                    mem[i] = mem[i + 1] + ans
                    stack.append(i)
                else:
                    mem[i] = mem[i + 1] + neededTime[i]
            else:
                mem[i] = mem[i + 1]
                stack.append(i) 
        return mem[0]