# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy

        # Move the fast pointer n+1 steps ahead
        for _ in range(n + 1):
            fast = fast.next

        # Move both pointers until the fast pointer reaches the end
        while fast:
            fast = fast.next
            slow = slow.next

        # Remove the nth node from the end
        slow.next = slow.next.next

        return dummy.next


# Example usage:
# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

# Initialize the Solution class
solution = Solution()

# Remove the 2nd node from the end
new_head = solution.removeNthFromEnd(head, 2)

# Print the modified linked list
while new_head:
    print(new_head.val, end=" ")
    new_head = new_head.next
