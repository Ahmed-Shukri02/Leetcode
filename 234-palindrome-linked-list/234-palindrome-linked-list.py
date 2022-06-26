# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # complexities:
        # Time: O(n)
        # Space: O(n)
        
        data_list = []
        length = 0
        
        current = head
        while current: # = while current != None
            data_list.append(current.val)
            length += 1
            current = current.next
        
        # compare last and first value
        for i in range(int(ceil(length/2))):
            if(data_list[i] != data_list[-i-1]): return False
        
        return True