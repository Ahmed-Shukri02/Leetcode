"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def validate(i0, i, j0, j):
            if i0 == i and j0 == j:
                return True
            print(i0 - i, j0 - j)
            val = grid[i0][j0]
            for i_n in range(i0, i + 1):
                for j_n in range(j0, j + 1):
                    if grid[i_n][j_n] != val:
                        return False
            return True

        ROWS, COLS = len(grid), len(grid[0])


        def dfs(node, size):
            i0, i, j0, j = size
            if not validate(i0, i, j0, j):
                # partition to 4
                mid_j, mid_i = (j + j0) // 2, (i + i0) // 2
                tl, tr = (i0, mid_i, j0, mid_j), (i0, mid_i, mid_j + 1, j)
                bl, br = (mid_i + 1, i, j0, mid_j), (mid_i + 1, i, mid_j + 1, j)

                node.topLeft, node.topRight, node.bottomLeft, node.bottomRight = (Node(1, False, None, None, None, None), 
                Node(1, False, None, None, None, None), Node(1, False, None, None, None, None), Node(1, False, None, None, None, None))
                dfs(node.topLeft, tl)
                dfs(node.topRight, tr)
                dfs(node.bottomLeft, bl)
                dfs(node.bottomRight, br)
                print(node.topLeft.val, node.topRight.val)
            else:
                node.val = grid[i0][j0]
                node.isLeaf = True

        n = Node(1, False, None, None, None, None)
        dfs(n, (0, ROWS - 1, 0, COLS - 1))
        return n



