class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        final = []
        length = len(candidates)
        def helper(currSum, curr, index):
            #bounding function
            if index >= length:
                return
            #bounding function
            if currSum > target:
                return
            elif currSum == target:
                final.append(curr)
                return
                
            # currSum <= target
            curr.append(candidates[index])
            # decide to include current number
            helper(currSum + candidates[index], [i for i in curr], index)
            
            curr.pop()
            # decide to not include current number:
            helper(currSum, [i for i in curr], index + 1)
        
        helper(0, [], 0)
        return final