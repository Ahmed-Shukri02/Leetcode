# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        curr1, curr2 = l1, l2
        while curr1.next or curr2.next:
            if not curr1.next:
                curr1.next = ListNode(0)
            if not curr2.next:
                curr2.next = ListNode(0)
            curr1 = curr1.next
            curr2 = curr2.next
        
        c1, c2 = l1, l2
        carry = 0   
        while c1.next and c2.next:
            ans = c1.val + c2.val + carry
            c1.val = ans % 10
            if ans - 10 >= 0:
                carry = 1
            else:
                carry = 0
            c1 = c1.next
            c2 = c2.next
        
        ans = c1.val + c2.val + carry
        c1.val = ans % 10
        if ans - 10 >= 0:
            c1.next = ListNode(1)
        
        return l1
