# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next

        return True


# Example usage:
# Create a linked list with a cycle: 3 -> 2 -> 0 -> -4 -> (points back to 2)
head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next  # Creates a cycle

# Initialize the Solution class
solution = Solution()

# Check if the linked list has a cycle
result = solution.hasCycle(head)

# Print the result
print(result)  # Output: True
