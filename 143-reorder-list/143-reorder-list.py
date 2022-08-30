# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # find middle
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        curr = slow.next
        prev = slow.next = None
        
        # reverse everything from middle onwards
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
            continue
        
        
        # go through both curr and head, inserting each 
        final = head
        while prev:
            nextFinal, nextCurr = final.next, prev.next
            final.next = prev
            prev.next = nextFinal
            
            final = nextFinal
            prev = nextCurr