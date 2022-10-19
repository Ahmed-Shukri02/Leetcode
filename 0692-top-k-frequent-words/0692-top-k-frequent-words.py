class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        
        hmap = {}
        for word in words:
            hmap[word] = hmap.get(word, 0) + 1
        arr = sorted([[occurance, key] for key, occurance in hmap.items()], key = lambda x: (-x[0], x[1]))
        return [i[1] for i in arr][0:k]
        