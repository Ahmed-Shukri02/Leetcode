class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # assume no local minima
        # binary search for position i where:
        # arr[i - 1] < arr[i] > arr [i + 1]
        # if arr[i - 1] > arr[i]: right side of peak, ignore right
        # if arr[i + 1] > arr[i]: left side of peak, ignore left
        
        length = len(arr)
        l, r = 0, length - 1
        while l <= r:
            i = (l + r) // 2
            if i > 0 and arr[i - 1] > arr[i]:
                r = i - 1
                continue
            elif i < length and arr[i + 1] > arr[i]:
                l = i + 1
                continue
            elif arr[i + 1] > arr[i] and arr[i - 1] > arr[i]:
                print("local minima: assumption incorrect")
                break
            else:
                return i
        
        return -1
                
            
        
        