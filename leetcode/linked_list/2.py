# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = []

        head = None
        current = None

        remaing_balance = 0
        while l1 is not None and l2 is not None:
            tmp_value = l1.val + l2.val + remaing_balance
            remaing_balance = 0
            if tmp_value >= 10:
                tmp_value -= 10
                remaing_balance = 1
            l1 = l1.next
            l2 = l2.next

            if head is None:
                head = ListNode(tmp_value)
                current = head
            else:
                current.next = ListNode(tmp_value)
                current = current.next

        while l1 is not None:
            tmp_value = l1.val + remaing_balance
            remaing_balance = 0
            if tmp_value >= 10:
                tmp_value -= 10
                remaing_balance = 1

            l1 = l1.next
            if head is None:
                head = ListNode(tmp_value)
                current = head
            else:
                current.next = ListNode(tmp_value)
                current = current.next
        while l2 is not None:
            tmp_value = l2.val + remaing_balance
            remaing_balance = 0
            if tmp_value >= 10:
                tmp_value -= 10
                remaing_balance = 1

            l2 = l2.next
            if head is None:
                head = ListNode(tmp_value)
                current = head
            else:
                current.next = ListNode(tmp_value)
                current = current.next

        if remaing_balance != 0:
            if head is None:
                head = ListNode(remaing_balance)
                current = head
            else:
                current.next = ListNode(remaing_balance)
                current = current.next
        return head
