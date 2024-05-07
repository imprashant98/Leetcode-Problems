def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # sourcery skip: extract-method
    if not ehad or not head.next:
        return head

    odd_head = odd = head
    even_head = even = head

    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next

        odd.next = even_head

        return odd_head
