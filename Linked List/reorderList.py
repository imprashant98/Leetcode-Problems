# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head):
        if not head or not head.next:
            return head

        # Step 1: Find the middle of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the linked list
        prev, current = None, slow
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        # Step 3: Merge the first half and the reversed second half
        first, second = head, prev
        while second.next:
            temp1, temp2 = first.next, second.next
            first.next, second.next = second, temp1
            first, second = temp1, temp2

        return head


# Example usage:
# Create a linked list: 1 -> 2 -> 3 -> 4
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

# Initialize the Solution class
solution = Solution()

# Reorder the linked list
solution.reorderList(head)

# Print the reordered linked list
while head:
    print(head.val, end=" ")
    head = head.next
