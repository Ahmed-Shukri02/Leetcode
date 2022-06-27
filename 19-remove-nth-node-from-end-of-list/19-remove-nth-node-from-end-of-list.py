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
        # Complexities:
        # Time: O(n)
        # Space: O(1)
        
        
        # find full length of linked list
        length = 0
        currL = head
        while currL:
            length += 1
            currL = currL.next
        
        # get to nth node
        prev, curr = None, head
        counter = 1
        while counter <= (length - n):
            prev = curr
            curr = curr.next
            counter += 1
        
        # set prev.next to curr.next. if 1 element list, set head to None
        if prev:
            prev.next = curr.next
        else:
            head = head.next
        
        return head