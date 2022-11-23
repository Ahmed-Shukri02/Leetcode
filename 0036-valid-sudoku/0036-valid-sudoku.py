class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        # O(n^2) time with O(n) space
        
        # create 19 hash maps
        cols = [{} for i in range(9)]
        
        squareMaps = {(0, 0): {}, (0, 1): {}, (0, 2): {},
                      (1, 0): {}, (1, 1): {}, (1, 2): {},
                      (2, 0): {}, (2, 1): {}, (2, 2): {}}
        
        
        for i, row in enumerate(board):
            row_hmap = {}
            for j, item in enumerate(row):
                # is item .?
                if item == ".":
                    continue
                  
                # is item in row hmap?
                if row_hmap.get(item, None):
                    return False
                # is item in corresponding col?
                elif cols[j].get(item, None):
                    return False
                
                squareMap = squareMaps[(i // 3, j // 3)]
                # is item in corresponding square?
                if squareMap.get(item, None):
                    return False
                
                row_hmap[item] = 1
                cols[j][item] = 1
                squareMap[item] = 1
                
                
        return True