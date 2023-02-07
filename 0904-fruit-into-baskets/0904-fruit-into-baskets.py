class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) <= 2:
            return len(fruits)
        m = 0
        l, r = 0, 0
        hmap = defaultdict(int)
        
        def remove(n):
            if n not in hmap:
                return
            if hmap[n] > 0:
                hmap[n] -= 1
            if hmap[n] == 0:
                del hmap[n]
        

        while r < len(fruits):
            if len(hmap) >= 2 and fruits[r] not in hmap:
                m = max(m, r - l)
                while l < r and len(hmap) >= 2:
                    remove(fruits[l])
                    l += 1
            hmap[fruits[r]] += 1
            r += 1

        return max(m, r - l)


        

            
