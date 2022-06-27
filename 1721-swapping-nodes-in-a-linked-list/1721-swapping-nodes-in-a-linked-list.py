# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # complexities:
        # Time: O(n)
        # Space: O(1)
        
        
        # search through list of n whilst caching value of k
        curr = head
        lowerVal = head
        length = 0
        while curr:
            if (length + 1) == k:
                lowerVal = curr
            length += 1
            curr = curr.next
        
        # search through list again to find upperVal
        upperVal = head
        curr2 = head
        idx = 0
        while curr2:
            curr2 = curr2.next
            if(idx + 1) == length - k:
                upperVal = curr2
            idx += 1
        
        # swap values
        lowerVal.val, upperVal.val = upperVal.val, lowerVal.val
        return head
            