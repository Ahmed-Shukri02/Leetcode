class UnionFind:
    def __init__(self, nodes):
        self.parents = [i for i in range(len(nodes))]
        self.rank = [1] * len(nodes)
        
    def find(self, node):
        while self.parents[node] != node:
            node = self.parents[node]
        return node        
    
    def union(self, node1, node2):
        root1, root2 = self.find(node1), self.find(node2)
        if root1 == root2:
            # this connection is redundant
            return [node1 + 1, node2 + 1]
        
        if self.rank[root1] > self.rank[root2]:
            self.parents[root2] = root1
            self.rank[root1] += self.rank[root2]
        else: # <=
            self.parents[root1] = root2
            self.rank[root2] += self.rank[root1]
        
        return None


class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        nodes = set()
        for i in edges:
            nodes.add(i[0] - 1)
            nodes.add(i[1] - 1)
        
        uf = UnionFind(nodes)
        
        for i, j in edges:
            res = uf.union(i - 1, j - 1)
            if res:
                return res
        
