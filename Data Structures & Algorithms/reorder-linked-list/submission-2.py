# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        if not head or not head.next : return

        temp = head
        print(f"temp is {temp.val}")

        while(temp.next and temp.next.next):
            start = temp
            prev = temp
            curr = temp.next
            print(f"loop rerun : curr is {curr.val}")

            while(curr.next):
                prev = curr
                curr = curr.next
                print(f"curr is {curr.val}")

            prev.next = None

            temp2 = start.next
            start.next = curr
            curr.next = temp2

            temp = temp2
            print(f"temp is {temp.val}")
        
        return

