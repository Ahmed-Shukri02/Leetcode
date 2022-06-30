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
        # Find lengths for each: O(n) time with O(1) space
        length1 = 0
        curr1 = l1
        while curr1.next:
            curr1 = curr1.next
            length1 += 1
            
        length2 = 0
        curr2 = l2
        while curr2.next:
            curr2 = curr2.next
            length2 += 1
            
        # if one length is larger than the other, replace it with zeros
        if length1 > length2:
            i = 0
            while i < length1-length2:
                curr2.next = ListNode(0, None)
                curr2 = curr2.next
                i += 1
        
        elif length2 > length1:
            i = 0
            while i < length2-length1:
                curr1.next = ListNode(0, None)
                curr1 = curr1.next
                i += 1    
            
        reverseSum = self.addTwoNumbersRecursion(l1, l1, l2)
        
        return reverseSum
        
    
    
    
    def addTwoNumbersRecursion(self, head, l1, l2, carryOne = False): 
        if l1.next and l2.next:
            # add 1 if carry is true
            if carryOne:
                sum1 = l1.val + l2.val + 1
            else:
                sum1 = l1.val + l2.val
            
            if sum1 >= 10:
                sum1 -= 10
                l1.val = sum1
                return self.addTwoNumbersRecursion(head, l1.next, l2.next, carryOne = True)
            
            else: 
                l1.val = sum1
                return self.addTwoNumbersRecursion(head, l1.next, l2.next)
            
        else: # if we are at last node, will be FINAL RETURN
            if carryOne:
                sum1 = l1.val + l2.val + 1
            else:
                sum1 = l1.val + l2.val
            
            if sum1 >= 10:
                sum1 -= 10
                l1.val = sum1
                # create a new node with value 1
                l1.next = ListNode(1, None)
                return head # FINAL RETURN
            
            else: 
                l1.val = sum1
                return head # FINAL RETURN
            