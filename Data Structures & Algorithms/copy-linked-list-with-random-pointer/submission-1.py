"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head : return None
        
        newNode2oldRandom = {}
        oldNode2newNode = {}

        newNode = Node(head.val, None, None)
        newNode2oldRandom[newNode] = head.random
        oldNode2newNode[head] = newNode
        
        temp = head
        newHead = newNode
        temp2 = newHead
        while(temp.next):
            temp = temp.next
            newNode = Node(temp.val, None, None)
            newNode2oldRandom[newNode] = temp.random
            oldNode2newNode[temp] = newNode
            
            temp2.next = newNode
            temp2 = newNode

        temp = newHead
        while(temp):
            oldRandom = newNode2oldRandom[temp]
            newRandom = oldNode2newNode[oldRandom] if(oldRandom) else None
            temp.random = newRandom

            temp = temp.next
            
        return newHead
