# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0, head)
        l, r = dummy, head
        for i in range(n):
            r = r.next
        
        while r:
            r = r.next
            l = l.next
        l.next = l.next.next
        return dummy.next
        