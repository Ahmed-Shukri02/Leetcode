class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points)<=2: return len(points)

        def slope(p1,p2):
            # Vertical line
            if p2[0]-p1[0] == 0:
                return inf
            return (p2[1]-p1[1]) / (p2[0]-p1[0])                

        res = 0
        for i in range(len(points)):
            count = defaultdict(int)
            for j in range(i+1,len(points)):
                count[slope(points[i],points[j])] += 1
            if count:
                res = max(res,max(count.values()))
        
        return res + 1