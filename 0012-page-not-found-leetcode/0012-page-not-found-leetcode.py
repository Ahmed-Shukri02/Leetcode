class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        final = ""
        while num - 1000 >= 0:
            final += "M"
            num -= 1000
        if num >= 900:
            final += "CM"
            num -= 900
        
        while num - 500 >= 0:
            final += "D"
            num -= 500
        if num >= 400:
            final += "CD"
            num -= 400
        
        while num - 100 >= 0:
            final += "C"
            num -= 100
        if num >= 90:
            final += "XC"
            num -= 90
            
        while num - 50 >= 0:
            final += "L"
            num -= 50
        if num >= 40:
            final += "XL"
            num -= 40
        
        while num - 10 >= 0:
            final += "X"
            num -= 10
        if num >= 9:
            final += "IX"
            num -= 9
        
        while num - 5 >= 0:
            final += "V"
            num -= 5
        if num >= 4:
            final += "IV"
            num -= 4
            
        while num - 1 >=0:
            final += "I"
            num -= 1
            
        return final
        