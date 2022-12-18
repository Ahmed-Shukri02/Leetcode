class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonically decreasing stack
        length = len(temperatures)
        stack = [(temperatures[0], 0)] # (temp, index)
        f = [0] * length
        
        for i in range(length):
            while stack and temperatures[i] > stack[-1][0]:
                f[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append((temperatures[i], i))
        
        return f