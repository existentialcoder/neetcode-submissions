# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getLengthOfListNode(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        length = 1

        while True:
            if not fast.next:
                break
            elif not fast.next.next:
                length += 1
                break

            length += 2

            fast = fast.next.next
        
        return length
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = self.getLengthOfListNode(head)
        
        if length == 1 and n == 1:
            return None

        node_to_stop = length - n

        curr = head
        pointer = 1

        if node_to_stop == 0:
            return head.next


        while curr:
            if pointer == node_to_stop:
                curr.next = curr.next.next

            pointer += 1
            curr = curr.next
        
        return head
