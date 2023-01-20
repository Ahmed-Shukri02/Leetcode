class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        f = set()
        hmap = {}
        def dfs(i, path):
            if i >= len(nums):
                if len(path) >= 2: f.add(tuple(path))
                return
            elif path and nums[i] < path[-1]:
                # force skip
                dfs(i + 1, path.copy())
                return
            
            # include or skip
            dfs(i + 1, path.copy())
            path.append(nums[i])
            dfs(i + 1, path.copy())

        dfs(0, [])
        return list(f)




