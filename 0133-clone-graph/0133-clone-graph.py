"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None

        hmap = {node.val: Node(node.val)}
        q = deque([node])
        while q:
            l = len(q)
            for i in range(l):
                n = q.popleft()
                for neigh in n.neighbors:
                    if neigh.val not in hmap:
                        hmap[neigh.val] = Node(neigh.val)
                        q.append(neigh)
                    hmap[n.val].neighbors.append(hmap[neigh.val])
        return hmap[node.val]
                    
