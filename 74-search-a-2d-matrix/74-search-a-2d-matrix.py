class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        columnsLength = len(matrix)
        rowLength = len(matrix[0])
        
        bot, top = 0, columnsLength - 1
        while bot <= top :
            row = (bot+top)//2
            if matrix[row][0] > target:
                top = row - 1
                continue
            elif matrix[row][-1] < target:
                bot = row + 1
                continue
            else:
                # do binary search
                l, r = 0, rowLength - 1
                while l <= r:
                    mid = (l+r)//2
                    if target > matrix[row][mid]:
                        l = mid + 1
                        continue
                    elif target < matrix[row][mid]:
                        r = mid - 1
                        continue
                    else:
                        return True
                return False
        return False
        