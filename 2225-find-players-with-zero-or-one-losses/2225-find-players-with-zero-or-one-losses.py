class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        hset = set()
        length = len(matches)
        hmap = {}
        for i in range(length):
            hset.add(matches[i][0])
            hset.add(matches[i][1])
            
            hmap[matches[i][1]] = hmap.get(matches[i][1], 0) + 1
        
        win, one = [], []
        for player in hset:
            if player not in hmap:
                win.append(player)
            elif hmap[player] == 1:
                one.append(player)
        
        return [sorted(win), sorted(one)]