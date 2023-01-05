class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Time: O(mn), space: O(m) where m is the number of sets with overlapping intervals
        # order the intervals
        points = sorted(points)
        sets = [points[0][1]]
        for i in range(1, len(points)):
            if points[i][0] <= sets[-1]:
                sets[-1] = min(points[i][1], sets[-1])
            else:
                sets.append(points[i][1])
        return len(sets)