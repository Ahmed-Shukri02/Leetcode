class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # start with string, do for loop
        length = len(s)
        s = [char for char in s]
        print(s)
        i = 0
        while True:
            end = i + k - 1
            if end >= length:
                end = length - 1
            # two pointer method from i to i +k to reverse
            l, r = i, end
            while r and l <= r:
                s[l], s[r] = s[r], s[l] # reverse
                l += 1 # increment
                r -= 1
            
            if end == length - 1: break
            
            i += (2 * k)
        
        return "".join(s)