class Solution(object):
    def numberOfWeakCharacters(self, properties):
        """
        :type properties: List[List[int]]
        :rtype: int
        """
        properties.sort(key=lambda x: (x[0], -x[1]))
        # properties[0] in increasing, properties[1] in decreasing
        stack = []
        counter = 0
        
        for a, d in properties:
            while stack and stack[-1] < d:
                stack.pop()
                counter += 1
            stack.append(d)
        return counter