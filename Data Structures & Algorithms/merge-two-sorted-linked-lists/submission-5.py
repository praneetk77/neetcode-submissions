# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        i, j = l1, l2

        temp = ListNode()
        head = temp

        while(i and j):
            if(i.val <= j.val):
                temp.next = i
                i = i.next
            else: 
                temp.next = j
                j = j.next
            
            temp = temp.next
        
        while(i):
            temp.next = i
            i = i.next
            temp = temp.next
        
        while(j):
            temp.next = j
            j = j.next
            temp = temp.next
        
        temp.next = None
        return head.next










            