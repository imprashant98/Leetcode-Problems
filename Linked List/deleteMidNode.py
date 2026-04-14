# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        slow = head
        fast = head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        return head

# Example usage:
# Input: head = [1,3,4,7,1,2,6]
# Output: [1,3,4,1,2,6]
head = ListNode(1, ListNode(3, ListNode(4, ListNode(7, ListNode(1, ListNode(2, ListNode(6)))))))
solution = Solution()
result = solution.deleteMiddle(head)
# To print the resulting linked list
current = result
while current:
    print(current.val, end=' ')
    current = current.next