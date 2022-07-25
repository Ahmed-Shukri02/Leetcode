class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        stack = []
        depth = 0
        for log in logs:
            if log == "../":
                if len(stack) != 0:
                    stack.pop()
                    depth -= 1
            elif log == "./":
                continue
            else:
                stack.append(log)
                depth += 1
        return depth