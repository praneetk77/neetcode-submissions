# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def fun(self, prevNode: Optional[ListNode], node: Optional[ListNode]) -> Optional[ListNode]:
        print(f"called with node = {node.val if node else "None"} and prevNode = {prevNode.val if prevNode else "None"}")
        if node is not None : 
            nextNode = node.next
            node.next = prevNode
            return self.fun(node, nextNode)
        else : 
            print(f"prevNode is {prevNode.val}, returning ")
            return prevNode

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        # if head.next == None: return head

        node = head
        nextNode = head.next
        isNNFalse = nextNode is None
        # print(f"called with node = {node.val} and isNextNode null = {isNNFalse}")

        return self.fun(None, head)


     