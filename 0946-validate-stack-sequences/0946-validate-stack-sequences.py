class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i, j = 0, 0
        while i < len(pushed):
            stack.append(pushed[i])
            i += 1
            
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1

        return j >= len(popped)
