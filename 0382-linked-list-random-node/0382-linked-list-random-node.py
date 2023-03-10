# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.m = 0
        self.head = head
        curr = head
        while curr:
            self.m += 1
            curr = curr.next

    def getRandom(self) -> int:
        n = random.randint(0, self.m - 1)
        curr = self.head
        while n > 0:
            curr = curr.next
            n -= 1
        return curr.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()