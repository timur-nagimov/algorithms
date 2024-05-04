import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        numbers = []
        for node in lists:
            while node:
                numbers.append(node.val)
                node = node.next

        heapq.heapify(numbers)

        pre_start = ListNode(None)
        curr = pre_start
        while numbers:
            val = heapq.heappop(numbers)
            curr.next = ListNode(val)
            curr = curr.next
        return pre_start.next
