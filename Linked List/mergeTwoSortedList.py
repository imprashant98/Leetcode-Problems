# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        current = dummy

        while l1 and l2:
            if l1.val < l2.val:
                current.next, l1 = l1, l1.next
            else:
                current.next, l2 = l2, l2.next

            current = current.next

        # If one of the lists is not empty, append the remaining nodes
        current.next = l1 or l2

        return dummy.next


# Example usage:
# Create two linked lists: list1 = 1 -> 2 -> 4, list2 = 1 -> 3 -> 4
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

# Initialize the Solution class
solution = Solution()

# Merge the two linked lists
merged_list = solution.mergeTwoLists(list1, list2)

# Print the merged linked list
while merged_list:
    print(merged_list.val, end=" ")
    merged_list = merged_list.next
