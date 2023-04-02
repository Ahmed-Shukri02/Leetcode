class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions = sorted(potions)
        
        for i in range(len(spells)):
            spell = spells[i]
            # do binary search to find lower bound of success
            l, r = 0, len(potions) - 1
            mid = 0
            while l <= r:
                mid = (l + r) // 2
                if potions[mid] * spell >= success:
                    r = mid - 1
                else:
                    l = mid + 1
            spells[i] = len(potions) - l 
        
        return spells
