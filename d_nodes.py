class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class ListSol:
    @staticmethod
    def hasCycle(head):
        # Check for edge cases
        if not head or not head.next:
            return False

        # Use two pointers, slow and fast
        slow = head.next
        fast = head.next.next

        while fast and fast.next:
            if slow == fast:
                return True

            # Move slow one step at a time
            slow = slow.next

            # Move fast two steps at a time
            fast = fast.next.next

        return False
