# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        c1 = l1; c2 = l2
        carry = 0
        prev1 = c1

        while(c1 and c2): 
            v1 = c1.val ; v2 = c2.val

            sum = v1+v2+carry
            num = sum%10
            carry = sum//10

            c1.val = num
            c2.val = num

            prev1 = c1
            c1 = c1.next
            c2 = c2.next
        
        if(c1) : 
            prev = c1
            while(c1):
                sum = c1.val + carry
                num = sum%10
                carry = sum//10

                c1.val = num
                prev = c1
                c1 = c1.next
            
            if(carry!=0): 
                newNode = ListNode(carry)
                prev.next = newNode
            
            return l1
        elif(c2):
            prev = c2
            while(c2):
                sum = c2.val + carry
                num = sum%10
                carry = sum//10

                c2.val = num
                prev = c2
                c2 = c2.next
            
            if(carry!=0): 
                newNode = ListNode(carry)
                prev.next = newNode
            
            return l2
        else: 

            if(carry!=0): 
                newNode = ListNode(carry)
                prev1.next = newNode
            return l1

            
            


        