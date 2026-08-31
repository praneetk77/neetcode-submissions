# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        curr = head

        while curr and curr.next: 
            prev = curr
            curr2 = curr.next

            while curr2.next:
                prev = curr2
                curr2 = curr2.next

            prev.next = None
            temp = curr.next
            curr.next = curr2
            curr2.next = temp

            curr = temp
        



        
        