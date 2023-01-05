class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        candidates = sorted(candidates)
        final, curr = [], []
        length = len(candidates)
        def helper(index, currSum):
            if currSum == target:
                final.append([i for i in curr])
                return
            
            if index >= length or currSum > target:
                return
                
            # if currSum < target
            # decide to include current number
            curr.append(candidates[index])
            helper(index + 1, currSum + candidates[index])
            
            # decide not to include current number: blacklist the number
            curr.pop()
            while index + 1 < length and candidates[index] == candidates[index + 1]:
                index += 1
            helper(index + 1, currSum)
        helper(0, 0)
        return final