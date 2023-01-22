class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def valid(s):
            if not s:
                return False
            l, r = 0, len(s) - 1
            while l <= r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True
        
        f = []
        def dfs(i, partition, arr):
            if i >= len(s):
                if valid(partition):
                    arr.append(partition)
                    f.append(arr)
                return
            
            # validate partition
            if valid(partition): 
                # add to partition or restart
                dfs(i + 1, partition + s[i], arr.copy())
                arr.append(partition)
                dfs(i + 1, s[i], arr.copy())
            else:
                # force add 
                dfs(i + 1, partition + s[i], arr.copy())


        
        dfs(0, "", [])
        return f

