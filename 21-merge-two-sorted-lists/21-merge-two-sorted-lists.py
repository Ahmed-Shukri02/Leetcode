# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        curr1, curr2 = list1, list2
        head = ListNode()
        copyCurr = head
        
        # edge case: both lists are empty
        if not list1 and not list2:
            return None
        
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                copyCurr.next = curr1
                curr1 = curr1.next
                copyCurr = copyCurr.next
                continue
            else:
                copyCurr.next = curr2
                curr2 = curr2.next
                copyCurr = copyCurr.next
                continue
        
        if curr1:
            copyCurr.next = curr1
        else:
            copyCurr.next = curr2
        return head.next
            
            