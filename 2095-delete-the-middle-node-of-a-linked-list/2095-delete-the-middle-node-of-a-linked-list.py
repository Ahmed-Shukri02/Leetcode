# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Complexities
        # Time: O(n)
        # Space: O(1)
        
        # first get to the middle of the linked list
        prev, curr = None, head
        # make a fast pointer to go to the end
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            prev = curr
            curr = curr.next
            
        # now curr is the middle node, curr.next is the next node and prev is the previous node
        # set prev.next to curr.next
        if prev:
            prev.next = curr.next
        else: # will only happen if there is a one-element linked list
            head = None
            
        return head
            