# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # min heap
        
        def heappush(h, node):
            # push node in based on its value
            h.append(node)
            curr = len(h)
            par = curr // 2

            while par >= 1 and h[par-1].val > h[curr-1].val:
                h[par-1], h[curr-1] = h[curr-1], h[par-1]
                curr = par
                par = curr // 2

        def heappop(h):
            # pop node
            l = len(h)
            if not h:
                return None
            h[0], h[l-1] = h[l-1], h[0]
            node = h.pop()

            curr = 1
            c1, c2 = curr * 2, (curr * 2) + 1
            while c2 <= len(h) and min(h[c1-1].val, h[c2-1].val) < h[curr-1].val:
                if h[c1-1].val < h[c2-1].val:
                    h[c1-1], h[curr-1] = h[curr-1], h[c1 - 1]
                    curr = c1
                else:
                    h[c2-1], h[curr-1] = h[curr-1], h[c2 - 1]
                    curr = c2
                c1, c2 = curr * 2, (curr * 2) + 1

            if c1 <= len(h) and h[c1-1].val < h[curr - 1].val:
                h[c1-1], h[curr-1] = h[curr-1], h[c1 - 1]
            
            return node
        
        heap = []

        for h in lists:
            curr = h
            while curr:
                heappush(heap, curr)
                curr = curr.next

            
        # first node
        head = heappop(heap)
        curr = head
        while heap:
            curr.next = heappop(heap)
            curr = curr.next
        if curr: curr.next = None

        return head