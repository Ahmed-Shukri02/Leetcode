class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:


        def valid(curr):
            if not curr or len(curr) > 3:
                return False
            if len(curr) > 1 and curr[0] == "0":
                return False
            return int(curr) < 256
        
        final = []
        def dfs(i, curr, path, dots):
            if i>= len(s) or dots == 3:
                if valid(curr + s[i:]) and dots == 3:
                    path += curr + s[i:]
                    final.append(path)
                return
            
            if valid(curr):
                # add . or not
                dfs(i + 1, s[i], path + curr + ".", dots + 1)
                dfs(i + 1, curr + s[i], path, dots)
            elif not curr:
                dfs(i + 1, curr + s[i], path, dots)

        dfs(0, "", "", 0)
        return final