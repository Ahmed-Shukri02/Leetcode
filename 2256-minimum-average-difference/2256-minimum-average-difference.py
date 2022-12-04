class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        # inclusive prefix sum and exclusive (regular) postfix sum
        length = len(nums)
        incPre, post = [0] * length, [0] * length
        incPre[0], post[length - 1] = nums[0], 0
        # build inclusive prefix sum
        for i in range(1, length):
            incPre[i] = incPre[i - 1] + nums[i]
        # build regular postfix sum
        for i in range(length - 2, -1 , -1):
            post[i] = post[i + 1] + nums[i + 1]
        
        # create array of differences of average
        final = [abs((incPre[i]//(i + 1)) - (post[i]//(length - i - 1))) for i in range(length - 1)]
        # append last element to avoid divide by 0 error
        final.append(abs(incPre[length - 1]/length))
        print(final)
        
        m = length - 1
        for i in range(length - 2, -1, -1):
            if final[i] <= final[m]:
                m = i
        return m
            