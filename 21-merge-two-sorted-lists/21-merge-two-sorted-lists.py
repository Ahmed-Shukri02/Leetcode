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
        root = ListNode()
        final = root
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                final.next = ListNode(curr1.val)
                final, curr1 = final.next, curr1.next
            else:
                final.next = ListNode(curr2.val)
                final, curr2 = final.next, curr2.next
        if curr1:
            final.next = curr1
        if curr2:
            final.next = curr2
        return root.next