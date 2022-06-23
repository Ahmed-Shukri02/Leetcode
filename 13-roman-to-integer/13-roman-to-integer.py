class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # total complexities:
        # Time: O(n), Space: O(1)
        
        totalInt = 0
        conversionDict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        
        # reverse string: time and space complexity of O(n) and O(1) respectively
        s = s[::-1]
        
        # search through each letter of word and add into num_dict: time and space complexity of O(n) and O(1) respectively
        i = 0
        length = len(s)
        while i < length:
            if(i == length - 1):
                totalInt += conversionDict[s[i]]
                i += 1
                continue
            
            # check if V, X, L, C, D and M has its corresponding precursor
            if (s[i] == "V") or (s[i] == "X"):
                if(s[i+1] == "I"):
                    totalInt += conversionDict[s[i]] - 1
                    i += 2
                else:
                    totalInt += conversionDict[s[i]]
                    i += 1
            
            elif(s[i] == "L") or (s[i] == "C"):
                if(s[i+1] == "X"):
                    totalInt += conversionDict[s[i]] - 10
                    i += 2
                else:
                    totalInt += conversionDict[s[i]]
                    i += 1
            
            elif (s[i] == "D") or (s[i] == "M"):
                if(s[i+1] == "C"):
                    totalInt += conversionDict[s[i]] - 100
                    i += 2
                else:
                    totalInt += conversionDict[s[i]]
                    i += 1
            # if not, simply add the value in
            else:
                totalInt += conversionDict[s[i]]
                i += 1
                
        return totalInt