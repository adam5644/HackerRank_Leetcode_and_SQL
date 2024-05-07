"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return root
        root.next = None
        this_level = [root]

        #print('this_level = ', this_level)

        while True:
            # print('-------------------')
            # print('len(this_level) = ', len(this_level))
            # for x in this_level:
            #     print('x.val = ', x.val)

            if not this_level[0].left: 
                break
            
            next_level = []
            for x in this_level:
                # print('x.left = ', x.left)
                # print('x.right = ', x.right)
                next_level.append(x.left)
                next_level.append(x.right)

            for i in range(len(next_level)-1):
                next_level[i].next = next_level[i+1]
            next_level[-1].next= None
            this_level = next_level

        return root