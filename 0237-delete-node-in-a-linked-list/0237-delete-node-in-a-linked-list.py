# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        if not node:
            return None
        
        tmp, prev = node, None
        hmap = {}
        while tmp and tmp.next:
            tmp.val = tmp.next.val
            
            hmap[tmp] = prev
            
            prev = tmp
            tmp = tmp.next
        
        if tmp:
            prev.next = None
        else:
            hmap[prev].next = None