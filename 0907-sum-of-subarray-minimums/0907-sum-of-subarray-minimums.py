class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        length = len(arr)
        mem = [0] * length
        stack = []
        
        for i in range(length):
            while stack and arr[i] < stack[-1][0]:
                stack.pop()
            if stack:
                mem[i] = mem[stack[-1][1]] + (i - stack[-1][1]) * arr[i]
            else:
                mem[i] = (i + 1) * arr[i]
            stack.append((arr[i], i))
        
        return sum(mem) % ((10 ** 9) + 7)