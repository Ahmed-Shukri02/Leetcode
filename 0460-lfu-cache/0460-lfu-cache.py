class LFUCache:

    def __init__(self, capacity: int):
        self.m = capacity
        self.hmap = {}
        self.vals = {}

        self.min = 0


    def get(self, key: int) -> int:
        val, count = self.vals.get(key, [-1, -1])
        if count == -1:
            return -1

        # update count
        self.remove(key)
        if count == self.min and not self.hmap[count]:
            self.min += 1
        self.add(key, val, count + 1)

        return val


    def put(self, key: int, value: int) -> None:
        if self.m <= 0:
            return
        
        if key in self.vals:
            self.vals[key] = [value, self.vals[key][1]]
            self.get(key)
            return
        elif len(self.vals) >= self.m:
            # at capacity, remove LRU num
            old_key = self.hmap[self.min].popitem(last=False)[0]
            self.remove(old_key)
            
            
        self.min = 1
        self.add(key, value, 1)

    def remove(self, key):
        count = self.vals.get(key, [0, 0])[1]
        if key in self.hmap[count]: del self.hmap[count][key]
        del self.vals[key]
        

    def add(self, key, val, count):
        if count not in self.hmap:
            self.hmap[count] = OrderedDict([])
        self.hmap[count][key] = None
        
        self.vals[key] = [val, count]




# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)