class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        #edge case
        if len(s1) > len(s2):
            return False
        
        s1_count, s2_count = [0] * 26, [0] * 26
        length = len(s1)
        # init first window
        for i in range(length):
            s1_count[ord(s1[i]) - ord("a")] += 1
            s2_count[ord(s2[i]) - ord("a")] += 1
        # do first check
        matches = 0
        for i in range(26):
            if s1_count[i] == s2_count[i]:
                matches += 1
        if matches == 26:
            return True
        
        l, r = 0, length
        while r < len(s2):
            l_index, r_index = ord(s2[l]) - ord("a"), ord(s2[r]) - ord("a")
            # minus whats on l
            s2_count[l_index] -= 1
            if s2_count[l_index] == s1_count[l_index] : matches += 1
            elif s2_count[l_index] + 1 == s1_count[l_index]: matches -= 1
            # add whats on r
            s2_count[r_index] += 1
            if s2_count[r_index] == s1_count[r_index] : matches += 1
            elif s2_count[r_index] - 1 == s1_count[r_index]: matches -= 1
            # do a check, if matching return true
            if r == 4: print(s1_count, s2_count)
            if matches == 26: return True
            # if not increment l and r by one
            l, r = l + 1, r + 1
        
        # after exhausting, return false
        return matches == 26