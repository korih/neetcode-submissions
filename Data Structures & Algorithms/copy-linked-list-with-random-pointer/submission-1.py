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
        mp = {}
        mp[None] = None

        curr = head
        while curr:
            node = Node(curr.val, None, None)
            mp[curr] = node
            curr = curr.next
        
        curr = head
        while curr:
            node = mp[curr]
            next_node = mp[curr.next]
            ran_node = mp[curr.random]
            node.next = next_node
            node.random = ran_node
            curr = curr.next
        
        return mp[head]        
