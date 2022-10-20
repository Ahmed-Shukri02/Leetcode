class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        def helper(y, x, facing):
            turns = {"N": ["W", "E"], "E": ["N", "S"], "S": ["E", "W"], "W": ["S", "N"]} # turns[i][0] = left turn ...[1] = right turn
            dydx = {"N": (1, 0), "E": (0, 1), "S": (-1, 0), "W": (0, -1)}
            for ins in instructions:
                if ins == "L":
                    facing = turns[facing][0]
                elif ins == "R":
                    facing = turns[facing][1]
                else:
                    y, x = y + dydx[facing][0] , x + dydx[facing][1]
            return (y, x, facing)
    
        y, x = 0, 0
        facing = "N"
        for i in range(4):
            y, x, facing = helper(y, x, facing)
            if y == 0 and x == 0: return True
        
        
        return y == 0 and x == 0