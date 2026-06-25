# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def fun(self, prevNode: Optional[ListNode], node: Optional[ListNode]) -> Optional[ListNode]:
        if node is not None : 
            nextNode = node.next
            node.next = prevNode
            return self.fun(node, nextNode)
        else : 
            return prevNode

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        return self.fun(None, head)


     