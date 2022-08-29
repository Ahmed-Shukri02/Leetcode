# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #edge case
        if not head:
            return head
        
        prev, curr = None, head
        while curr and curr.next:
            # cache next
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        # do one more time for new head
        
        curr.next = prev
        return curr
        