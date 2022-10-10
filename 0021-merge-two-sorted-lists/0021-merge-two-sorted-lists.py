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
        
        if not list1 and not list2:
            return None
        
        final = ListNode()
        tmp = final
        
        while list1 and list2:
            if list1.val >= list2.val:
                tmp.val = list2.val
                list2 = list2.next
            else:
                tmp.val = list1.val
                list1 = list1.next
            
            tmp.next = ListNode()
            tmp = tmp.next
        
        if list1:
            tmp.val = list1.val
            tmp.next = list1.next
        if list2:
            tmp.val = list2.val
            tmp.next = list2.next
            
        return final