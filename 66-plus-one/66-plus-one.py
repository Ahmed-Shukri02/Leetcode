class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        length = len(digits)
        
        # reverse: two pointer method
        l, r = 0, length - 1
        while r > l:
            digits[r], digits[l] = digits[l], digits[r]
            l += 1
            r -= 1
        
        i, carry = 0, 0
        while i < length:
            if i == 0:
                total = digits[i] + 1
            else:
                total = digits[i] + carry
            
            carry = total // 10
            
            if carry:
                digits[i] = total % 10
                if i == length - 1:
                    digits.append(1)
                    length += 1
                    break
            else:
                digits[i] = total
            
            
            i += 1
        
        
        
        # re-reverse list
        l, r = 0, length - 1
        while r > l:
            digits[r], digits[l] = digits[l], digits[r]
            l += 1
            r -= 1
        
        return digits
                
                
        
        
        
        
        
        