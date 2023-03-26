class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        ranges = sorted(ranges)
        new_interval = ranges[0]
        f = []
        for interval in ranges:
            # check if they overlap
            if max(new_interval) >= min(interval):
                # overlap
                new_interval = [min(new_interval[0], interval[0]), max(new_interval[1], interval[1])]
            else:
                f.append(new_interval.copy())
                new_interval = interval
        f.append(new_interval)

        return (2 ** len(f)) % ((10**9) + 7)