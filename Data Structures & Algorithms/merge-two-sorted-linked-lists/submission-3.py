# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def iterativeImpl(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
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
    
    def fun(self, node1: Optional[ListNode], node2: Optional[ListNode]):
        if(not node1 or not node2): return
        print(f"^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        print(f"Start : node1.val: {node1.val} node2.val: {node2.val}")

        if(node1.val <= node2.val):
            print(f"1. node1: {node1.val}, node2: {node2.val}")
            if node1.next:
                print(f"2. node1.next: {node1.next.val}")
                if(node1.next.val <= node2.val):
                    print(f"3. node2.val: {node2.val}")
                    self.fun(node1.next, node2)
                else:
                    print(f"4. node2.val: {node2.val}")
                    temp = node1.next
                    node1.next = node2
                    self.fun(temp, node2)
            else: 
                print(f"5.")
                node1.next = node2
        else:
            print(f"6. node1: {node1.val}, node2: {node2.val}")
            if node2.next:
                print(f"7. node2.next: {node2.next.val}")
                if(node2.next.val <= node1.val):
                    print(f"8. node1.val: {node1.val}")
                    self.fun(node1, node2.next)
                else:
                    print(f"9. node1.val: {node1.val}")
                    temp = node2.next
                    node2.next = node1
                    self.fun(node1, temp)
            else: 
                print(f"10.")
                node2.next = node1



    def recursiveImpl(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1: 
            if list2: 
                self.fun(list1, list2)
                if(list1.val<=list2.val): return list1
                else: return list2
            else: return list1
        else:
            if list2: return list2
            else: return None
    def recursiveImpl2(self, l1, l2):

        if not l1:
            return l2

        if not l2:
            return l1

        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        return self.recursiveImpl2(list1, list2)
        

        