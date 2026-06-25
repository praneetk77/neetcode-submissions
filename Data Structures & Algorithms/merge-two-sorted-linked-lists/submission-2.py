# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if(not list1): return list2
        elif(not list2): return list1
        curr1 = list1; curr2 = list2; prev1 = None; prev2 = None;

        while curr1 and curr2 : 
            if(curr1.val <= curr2.val):
                while(curr1 and curr1.val <= curr2.val):
                    prev1 = curr1
                    curr1 = curr1.next
                prev1.next = curr2
            else: 
                while(curr2 and curr2.val <= curr1.val):
                    prev2 = curr2
                    curr2 = curr2.next
                prev2.next = curr1
        
        if(list1.val<=list2.val): return list1
        else: return list2

        