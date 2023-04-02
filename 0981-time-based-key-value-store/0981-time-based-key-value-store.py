class TimeMap:

    def __init__(self):
        self.hmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hmap:
            self.hmap[key] = [(0, "")]
        self.hmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.hmap.get(key, [(0, "")])
        # binary search for timestamp w
        l , r = 0, len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid][0] == timestamp:
                return arr[mid][1]
            elif arr[mid][0] > timestamp:
                r = mid - 1
            else:
                l = mid + 1
        return arr[(l + r) // 2][1]



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)