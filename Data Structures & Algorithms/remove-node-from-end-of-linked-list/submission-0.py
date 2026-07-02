# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        size = 0
        curr = head
        while(curr):
            size += 1
            curr = curr.next
        
        ind = size - n

        if(ind==0) : return head.next
        
        prev = None
        curr = head
        x = 0
        while(curr):
            if(x==ind):
                temp = curr.next
                prev.next = temp
                break
            else: 
                x += 1
                prev = curr
                curr = curr.next

        return head
                