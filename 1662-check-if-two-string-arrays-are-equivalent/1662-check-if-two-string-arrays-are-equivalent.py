class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        w1, w2 = "", ""
        for word in word1:
            w1 += word
        for word in word2:
            w2 += word
        return w1 == w2