class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # build a bi-directional graph for mapping
        adj = {}
        for i in range(len(s1)):
            if s1[i] not in adj: adj[s1[i]] = []
            if s2[i] not in adj: adj[s2[i]] = []
            adj[s1[i]].append(s2[i])
            adj[s2[i]].append(s1[i])
        
        # contain mem for every character
        mem = [None] * 26
        # do bfs for each character
        final = ""
        for char in baseStr:
            if char not in adj:
                final += char
                continue
            index = ord(char) - ord("a")
            if mem[index] == None:
                # do bfs
                q = deque([char])
                smallestChar = ord(char)
                bl = set([char])
                while q:
                    l = len(q)
                    for i in range(l):
                        for neigh in adj[q[i]]:
                            if neigh in bl:
                                continue
                            bl.add(neigh)
                            q.append(neigh)
                    for i in range(l):
                        smallestChar = min(smallestChar, ord(q.popleft()))
                mem[index] = chr(smallestChar)
            
            final += mem[index]
        
        return final