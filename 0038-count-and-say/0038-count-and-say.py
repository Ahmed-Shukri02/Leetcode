class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        def helper(a):
            final = ""
            counter = 1
            
            for i in range(1, len(a)):
                if a[i - 1] == a[i]:
                    counter += 1
                else:
                    final += str(counter) + a[i - 1] 
                    counter = 1
            
            final += str(counter) + a[-1]
            return final
        
        ans = "1"
        for i in range(1, n):
            ans = helper(ans)
        
        return ans