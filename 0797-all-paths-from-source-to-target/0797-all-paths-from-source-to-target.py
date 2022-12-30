class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """

        n = len(graph) - 1
        final = []

        def dfs(i, path):
            if i == n:
                path.append(i)
                final.append(path)
                return
            
            path.append(i)
            for neigh in graph[i]:
                dfs(neigh, [i for i in path])
        
        dfs(0, [])
        return final


            