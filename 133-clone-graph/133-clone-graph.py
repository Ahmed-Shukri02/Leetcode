"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        
        hmap = {}
        if not node:
            return node
        
        def dfs(node):

            new = Node(node.val)
            hmap[node] = new
            
            for neighbour in node.neighbors:
                if hmap.get(neighbour, None):
                    # already visited, just add to neigbours
                    new.neighbors.append(hmap[neighbour])
                    continue
                else:
                    new.neighbors.append(dfs(neighbour))
            return new
        
        return dfs(node)