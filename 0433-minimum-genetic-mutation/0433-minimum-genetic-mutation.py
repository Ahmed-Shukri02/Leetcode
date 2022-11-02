class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        length = len(bank)
        
        def dfs(i, hset):
            if bank[i] in hset:
                return float("inf")
            elif bank[i] == end:
                return 0
            
            hset.add(bank[i])
            
            minm = float("inf")
            for j in range(length):
                mis = 0
                for k in range(8):
                    if bank[i][k] != bank[j][k]:
                        mis += 1
                if mis == 1: 
                    ans = dfs(j, hset)
                    minm = min(minm, 1 + ans)
            
            hset.remove(bank[i])
            return minm
        
        minm = float("inf")
        for j in range(length):
            mis = 0
            for k in range(8):
                if start[k] != bank[j][k]:
                    mis += 1
            if mis == 1: minm = min(minm, 1 + dfs(j, set()))
        
        return -1 if minm == float("inf") else minm
            
            
            
        
        