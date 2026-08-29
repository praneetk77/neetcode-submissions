# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if(not head): return False
        # t1, t2 = head, head

        # while(True):
        #     t1 = t1.next
        #     if(not t1): return False

        #     t2 = t2.next
        #     if(not t2): return False
        #     t2 = t2.next
        #     if(not t2): return False

        #     if(t1 == t2): return True
        
        # return False

        s = set()
        temp = head
        s.add(temp)

        while(True):
            temp = temp.next
            if(not temp): return False

            if(temp in s): return True
            else: s.add(temp)
        
        return True



