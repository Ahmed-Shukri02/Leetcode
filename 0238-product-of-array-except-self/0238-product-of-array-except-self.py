class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # generate post and prefix products
        length = len(nums)
        post, pre = [1] * length, [1] * length
        
        for i in range(1, length):
            pre[i] = nums[i - 1] * pre[i - 1]
    
        for i in range(length - 2, -1, -1):
            post[i] = nums[i + 1] * post[i + 1]
        
        final = []
        for i in range(length):
            final.append(pre[i] * post[i])
        
        return final