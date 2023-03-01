class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def heapfix(nums, i):
            curr = i
            c1, c2 = curr * 2, (curr * 2) + 1
            while c2 < len(nums) and nums[curr] > min(nums[c1], nums[c2]):
                if nums[c1] < nums[c2]:
                    nums[c1], nums[curr] = nums[curr], nums[c1]
                    curr = c1
                    c1, c2 = curr * 2, (curr * 2) + 1
                else:
                    nums[c2], nums[curr] = nums[curr], nums[c2]
                    curr = c2
                    c1, c2 = curr * 2, (curr * 2) + 1
            if c1 < len(nums) and nums[curr] > nums[c1]:
                nums[c1], nums[curr] = nums[curr], nums[c1]
        
        
        def heapify(nums):
            i = len(nums)
            while i >= 0:
                heapfix(nums, i)
                i -= 1
                   
        def heappop(nums):
            l = len(nums)
            ans = nums[0]
            nums[0], nums[l-1] = nums[l-1], float("inf")
            heapfix(nums, 0)
            return ans



        heapify(nums)



        f = []
        for i in range(len(nums)):
            f.append(heappop(nums))
        return f