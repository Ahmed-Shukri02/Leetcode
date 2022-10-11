# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        
        hmap = set()
        tmp = head
        while tmp:
            if tmp in hmap:
                return tmp
            hmap.add(tmp)
            tmp = tmp.next
        return None