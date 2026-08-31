# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 1
        temp = head

        while(temp.next):
            length += 1
            temp = temp.next
        
        ind = length - n

        if(ind==0): return head.next

        curr_ind = 1
        prev = head
        temp = head.next

        while(curr_ind < ind):
            curr_ind += 1
            prev = temp
            temp = temp.next
        
        temp2 = temp.next
        temp.next = None
        prev.next = temp2

        return head

        