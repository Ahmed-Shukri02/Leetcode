class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        length = len(paths)
        hmap = {}
        
        def getContent(f):
            f = f.split("(")
            return f[1][:-1]
        
        final = {}
        for i in range(length):
            split = paths[i].split(" ")
            #hmap[split[0]] = split[1:]
            for path in split[1:]:
                content = getContent(path)
                finalPath = (split[0] + "/" + path).split("(")[0]
                if content not in final:
                    final[content] = [finalPath]
                else:
                    final[content].append(finalPath)
                
        arr = []
        for val in final.values():
            if len(val) > 1:
                arr.append(val)
        return arr
            