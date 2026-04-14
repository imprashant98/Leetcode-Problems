
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        while l1 or l2 or carry:
            # Get values
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate sum
            total = val1 + val2 + carry
            print(f"Adding {val1} + {val2} + carry {carry} = {total}")
            carry = total // 10
            print(f"New carry: {carry}")
            digit = total % 10
            print(f"Digit to store: {digit}")
            
            # Create new node
            current.next = ListNode(digit)
            current = current.next
            
            # Move pointers
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next
    

# Example usage:
# l1: 2 -> 4 -> 3
# l2: 5 -> 6 -> 4
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
solution = Solution()
result = solution.addTwoNumbers(l1, l2)