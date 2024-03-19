from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True


links = [3, 2, 0, -4]
pos = 1
head = ListNode(links[0])
current = head
cycle = None
for i in range(1, len(links)):
    current.next = ListNode(links[i])
    current = current.next
    if i == pos:
        cycle = current
current.next = cycle
solution = Solution()
print(solution.hasCycle(head))
