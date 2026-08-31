# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if(not l1):
            print("her1")
            return l2
        if(not l2): 
            print("her2")
            return l1

        rem = 0
        ol1 = l1
        ol2 = l2

        init_sum = l1.val + l2.val
        s = init_sum % 10
        rem = init_sum // 10

        l1.val = s
        l2.val = s
        print(f"both vals updated to {l1.val}")

        prev1 = l1
        prev2 = l2

        l1 = l1.next
        l2 = l2.next


        while(l1 and l2):
            init_sum = l1.val + l2.val + rem
            s = init_sum%10
            rem = init_sum//10

            l1.val = s
            l2.val = s
            print(f"both vals updated to {l1.val}")
            prev1 = l1
            prev2 = l2
            l1 = l1.next
            l2 = l2.next

        take_l1 = False
        
        while(l1):
            take_l1 = True
            init_sum = l1.val + rem
            s = init_sum%10
            rem = init_sum//10

            l1.val = s
            print(f"l1 val updated to {l1.val}")
            prev1 = l1
            l1 = l1.next
        
        while(l2):
            init_sum = l2.val + rem
            s = init_sum%10
            rem = init_sum//10

            l2.val = s
            print(f"l2 val updated to {l2.val}")
            prev2 = l2
            l2 = l2.next
        
        if(rem > 0):
            newNode = ListNode(rem)
            if(take_l1):
                prev1.next = newNode
                return ol1
            else:
                prev2.next = newNode
                return ol2
        else:
            if(take_l1):
                return ol1
            else:
                return ol2
