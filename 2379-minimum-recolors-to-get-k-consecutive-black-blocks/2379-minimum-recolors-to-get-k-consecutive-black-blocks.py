class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        length = len(blocks)
        rs = mv = blocks[:k].count("B")
        for i in range(1, length - k + 1):
            # remove last element, add next elem
            if blocks[i - 1] == "B": mv -= 1
            if blocks[i + k - 1] == "B": mv += 1
                
            rs = max(rs, mv)
        
        return k - rs 