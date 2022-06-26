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
        # try algorithm with time complexity of O(n) and space complexity of O(1):
        
        # use 2 pointer method to reach the midpoint of the linked list
        pf, ps = head, head
        
        while pf and pf.next: # while fast pointer is not pointing to none
            pf = pf.next.next
            ps = ps.next
        
        # reverse everything from the midpoint onwards
        prev, current = None, ps
        
        while current: #while current pointer is not pointing to none
            nextTemp = current.next # temporarily store next node for access
            current.next = prev
            prev = current
            current = nextTemp
        
        # loop ends when current = None and so previous is the last node. This can be used
        
        while prev:
            if(prev.val != head.val): return False
            else:
                prev = prev.next
                head = head.next
        return True
        
            