class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adjMap = {}
        for i in prerequisites:
            if i[0] in adjMap:
                adjMap[i[0]].append(i[1])
            else:
                adjMap[i[0]] = [i[1]]
        
        for i in range(numCourses):
            if i not in adjMap:
                adjMap[i] = []
        
        
        visited = [False] * numCourses
        
        def dfs(key):
            if visited[key]:
                return False
            if not adjMap[key]: # if adjMap[key] == []
                return True
            
            visited[key] = True
            
            # run for each neighbour
            for nei in adjMap[key]:
                if not dfs(nei):
                    return False
            visited[key] = False
            adjMap[key] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i): return False
        return True