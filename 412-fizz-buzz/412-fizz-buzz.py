class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # complexities:
        # Time: O(n)
        # Space: O(n)
        
        final = []
        
        for i in range(n):
            final_text = ""
            if((i+1) % 3 == 0): final_text += "Fizz"
            if ((i+1) % 5 == 0): final_text += "Buzz"
                
            if(final_text == ""): final_text = str(i+1)
            final.append(final_text)
        
        return final