class Solution:
    def longestPalindrome(self, words: List[str]) -> int:        
        
        hmap = {}
        for word in words:
            hmap[word] = hmap.get(word, 0) + 1
            
        ans, centre = 0, False
        
        for word, count in hmap.items():
            if word[0] == word[1]:
                if count % 2 == 0:
                    ans += count
                else:
                    ans += count - 1 # makes sure to include all even pairs into answer, leaving out centre
                    centre = True 
                    
            elif word[0] > word[1]: # just to stop this running with both symmetrical words (ie. "ab" and "ba"). it would run for both if I wrote word[0] != word[1]
                ans += 2 * min(count, hmap.get(word[::-1], 0))
        if centre: ans += 1
            
        return ans * 2